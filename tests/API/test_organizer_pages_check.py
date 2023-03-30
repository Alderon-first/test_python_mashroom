import os

from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser

from test_python_mashroom.API.utils.base_session import BaseSession

load_dotenv()


def test_login(demoshop_api):
    demoshop_api.open('')

