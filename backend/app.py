from contextlib import asynccontextmanager
from datetime import datetime, timezone
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from db import PostgresWrapper
import env
from log import get_logger
from mco.data import DataWrapper
from mco.router import router as mco_router


logger = get_logger(__name__)


scheduler = BackgroundScheduler()
data_refresh_job = scheduler.add_job(DataWrapper.refresh_data, CronTrigger.from_crontab('0/5 * * * *'))


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup tasks
    logger.info('Triggering Postgres startup script')
    PostgresWrapper.execute_startup()
    logger.info('Completed Postgres startup script')
    logger.info('Triggering data refresh job')
    DataWrapper.refresh_data()
    logger.info('Completed data refresh job')
    logger.info('Triggering background scheduler')
    scheduler.start()
    logger.info('Background scheduler is running')
    # execution
    yield
    # shutdown tasks
    pass


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(mco_router)


@app.get('/')
async def root():
    return Response(content=datetime.now(timezone.utc).isoformat())


if __name__ == '__main__':
    uvicorn.run(app, host=env.API_HOST, port=env.API_PORT, workers=env.API_WORKERS)
