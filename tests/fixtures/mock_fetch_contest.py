import pytest

from tests.helpers import fetch_contest


@pytest.fixture
def mock_fetch_contest(mocker):
    yield mocker.patch('src.services.SportService.fetch_contest', fetch_contest)