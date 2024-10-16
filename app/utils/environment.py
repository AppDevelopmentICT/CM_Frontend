import os
from dotenv import load_dotenv

load_dotenv()

ALGORITHM = os.getenv('ALGORITHM')
SECRET_KEY = os.getenv('SECRET_KEY')
API_VERSION = os.getenv('API_VERSION')

MAIL_USERNAME=os.getenv('MAIL_USERNAME')
MAIL_FROM=os.getenv('MAIL_FROM')
MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
MAIL_PORT=os.getenv('MAIL_PORT')
MAIL_SERVER=os.getenv('MAIL_SERVER')
MAIL_TLS=os.getenv('MAIL_TLS')
MAIL_SSL=os.getenv('MAIL_SSL')

POCKETBASE=os.getenv("PB_BASEURL")