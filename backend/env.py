from dotenv import load_dotenv
load_dotenv()

import os
API_HOST = os.getenv('API_HOST') or '0.0.0.0'
API_PORT = int(os.getenv('API_PORT') or '8080')
API_WORKERS = int(os.getenv('API_WORKERS') or '1')

DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']

ENV_NAME = os.getenv('ENV_NAME')
