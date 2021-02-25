import pytest

from tests.helpers import update_score


@pytest.fixture
def mock_update_score(mocker):
    yield mocker.patch('src.services.SportService.update_score', update_score)
