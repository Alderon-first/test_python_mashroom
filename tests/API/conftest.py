import os

import pytest
from dotenv import load_dotenv
from test_python_mashroom.API.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def stend_api():
    return BaseSession(os.getenv('STEND_URL_API'))



