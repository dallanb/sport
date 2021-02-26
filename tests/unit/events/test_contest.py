import pytest

from src import events, ManualException, services


def test_contest_contest_ready_sync(reset_db, pause_notification, mock_fetch_contest, mock_fetch_course,
                                    mock_fetch_score, mock_update_score):
    """
    GIVEN 0 member instance, 0 wallet instance and 0 stat instance in the database
    WHEN directly calling event account handle_event account_active
    THEN event account handle_event account_active adds 1 member, 1 wallet and 1 stat instance into the database
    """

    # We will temporary make the default sport as golf for this test
    temp_sport_name = pytest.sport_name

    sports = services.SportService().find()
    pytest.sport = sports.items[0]
    pytest.sport_name = sports.items[0].name

    key = 'contest_ready'
    value = {
        'uuid': str(pytest.contest_uuid)
    }

    try:
        events.Contest().handle_event(key=key, data=value)
    except ManualException:
        raise Exception('test failed')
    finally:
        pytest.sport_name = temp_sport_name
        pytest.sport = None
