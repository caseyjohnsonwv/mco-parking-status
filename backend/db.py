from contextlib import contextmanager
from typing import Generator
import psycopg2
from sqlalchemy import create_engine, Engine
from sqlalchemy.pool import Pool
from sqlalchemy.orm import DeclarativeBase, Session
import env
from log import get_logger


logger = get_logger(__name__)



class Base(DeclarativeBase):
    pass



class PostgresWrapper:
    def build_uri() -> str:
        # return f"postgresql+psycopg2://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}"
        return f"sqlite:///app.db"
    
    @contextmanager
    def get_engine(echo:bool=False) -> Generator[Engine, None, None]:
        engine = create_engine(PostgresWrapper.build_uri(), echo=echo, pool_size=1)
        yield engine
        engine.dispose()

    @contextmanager
    def connect(echo:bool=False) -> Generator[Session, None, None]:
        with PostgresWrapper.get_engine(echo=echo) as engine:
            assert isinstance(engine, Engine)
            session = Session(engine)
            yield session
            session.close()

    def execute_startup():
        with PostgresWrapper.get_engine() as engine:
            Base.metadata.drop_all(engine)
            logger.info('Dropped DB tables')
            Base.metadata.create_all(engine)
            logger.info('Created DB tables')
