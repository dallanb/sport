import pytest


@pytest.fixture(scope="function")
def pause_notification():
    return True
