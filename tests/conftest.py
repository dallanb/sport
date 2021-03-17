from uuid import uuid4

import pytest

from .fixtures import *


def pytest_configure(config):
    pytest.sport = None
    pytest.sport_name = 'tennis'
    pytest.user_uuid = uuid4()
    pytest.league_uuid = uuid4()
    pytest.location_uuid = uuid4()
    pytest.member_uuid = uuid4()
    pytest.other_member_uuid = uuid4()
    pytest.contest_uuid = uuid4()
    pytest.score_uuid = uuid4()
