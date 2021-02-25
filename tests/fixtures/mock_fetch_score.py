import pytest

from tests.helpers import fetch_score


@pytest.fixture
def mock_fetch_score(mocker):
    yield mocker.patch('src.services.SportService.fetch_score', fetch_score)
