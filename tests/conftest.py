from uuid import uuid4

import pytest

from .fixtures import *


def pytest_configure(config):
    pytest.sport = None
    pytest.sport_name = 'tennis'
    pytest.user_uuid = uuid4()
