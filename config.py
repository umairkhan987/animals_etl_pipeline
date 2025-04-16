import os
from dotenv import load_dotenv

load_dotenv()


BASE_URL = f'{os.getenv("BASE_URL")}/animals/v1'
