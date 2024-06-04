import os
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(__file__)
path_fixture_json = os.path.join(ROOT_DIR, 'fixtures', 'catalog_data.json')

load_dotenv()


def settings_bd():
    return os.getenv('PASSWORD')
