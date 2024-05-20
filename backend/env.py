from dotenv import load_dotenv
load_dotenv()

import os
API_HOST = os.getenv('API_HOST') or '0.0.0.0'
API_PORT = int(os.getenv('API_PORT') or '8080')
API_WORKERS = int(os.getenv('API_WORKERS') or '1')
