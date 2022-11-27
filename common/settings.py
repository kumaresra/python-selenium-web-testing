# settings.py
import os
from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv


def load_env():
    print("Loading from env file")
    current_dir = Path(__file__)
    print("current_dir" +f'{current_dir}')
    base_path = next(p for p in current_dir.parents if p.name == "python-selenium-web-testing")
    project_dir = join(dirname(base_path), 'python-selenium-web-testing')
    dotenv_path = project_dir + '/.env'
    print("dotenv_path: " +f'{dotenv_path}')
    load_dotenv(dotenv_path)


def getTestUsername():
    return os.environ.get("TEST_USER")

def getTestPassword():
    return os.environ.get("TEST_USER_PASS")


    
