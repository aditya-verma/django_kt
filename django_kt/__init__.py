import os

from dotenv import load_dotenv


def load_dotenv_local():
    if os.environ.get('DJANGO_KT_IS_DEBUG', True):
        load_dotenv(override=True)
    else:
        load_dotenv(dotenv_path='/etc/django_kt/.env', override=True)
