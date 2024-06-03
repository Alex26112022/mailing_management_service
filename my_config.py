import os
from dotenv import load_dotenv

load_dotenv()


def settings_bd():
    return os.getenv('PASSWORD')
