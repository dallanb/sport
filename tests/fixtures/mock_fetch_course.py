import pytest

from tests.helpers import fetch_course


@pytest.fixture
def mock_fetch_course(mocker):
    yield mocker.patch('src.services.SportService.fetch_course', fetch_course)
