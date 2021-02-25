import pytest

from src import services


@pytest.fixture(scope="function")
def seed_sport():
    pytest.sport = services.SportService().create(name=pytest.sport_name)

