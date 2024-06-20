import os
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(__file__)
path_fixture_json = os.path.join(ROOT_DIR, 'fixtures', 'catalog_data.json')
path_blog_fixture_json = os.path.join(ROOT_DIR, 'fixtures', 'blog_data.json')

load_dotenv()

yandex_user = os.getenv('YANDEX_USER')
yandex_password = os.getenv('YANDEX_PASSWORD')


def settings_bd():
    return os.getenv('PASSWORD')
