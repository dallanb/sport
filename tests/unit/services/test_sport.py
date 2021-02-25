import pytest

from src import services, ManualException
from tests.helpers import generate_uuid

sport_service = services.SportService()


###########
# Find
###########
def test_sport_find(reset_db, pause_notification):
    """
    GIVEN 1 sport instance in the database
    WHEN the find method is called
    THEN it should return 1 sport
    """
    sports = sport_service.find()

    assert sports.total == 1
    assert len(sports.items) == 1


def test_sport_find_by_uuid(reset_db, pause_notification, seed_sport):
    """
    GIVEN 1 sport instance in the database
    WHEN the find method is called with uuid
    THEN it should return 1 sport
    """

    sports = sport_service.find(uuid=pytest.sport.uuid)

    assert sports.total == 1
    assert len(sports.items) == 1
    sport = sports.items[0]
    assert sport.uuid == pytest.sport.uuid


def test_sport_find_by_name():
    """
    GIVEN 1 sport instance in the database
    WHEN the find method is called with name
    THEN it should return as many sport exist for that name
    """

    sports = sport_service.find(name=pytest.sport_name)

    assert sports.total == 1
    assert len(sports.items) == 1


def test_sport_find_w_pagination(reset_db, pause_notification, seed_sport):
    """
    GIVEN 2 sport instance in the database
    WHEN the find method is called with valid pagination
    THEN it should return the number of sports defined in the pagination arguments
    """

    sports_0 = sport_service.find(page=1, per_page=1)
    assert sports_0.total == 2
    assert len(sports_0.items) == 1

    sports_1 = sport_service.find(page=2, per_page=1)
    assert sports_1.total == 2
    assert len(sports_1.items) == 1

    sports = sport_service.find(page=1, per_page=2)
    assert sports.total == 2
    assert len(sports.items) == 2


def test_sport_find_w_bad_pagination():
    """
    GIVEN 2 sport instance in the database
    WHEN the find method is called with invalid pagination
    THEN it should return the 0 sport
    """
    sports = sport_service.find(page=3, per_page=3)
    assert sports.total == 2
    assert len(sports.items) == 0


def test_sport_find_by_non_existent_column():
    """
    GIVEN 2 sport instance in the database
    WHEN the find method is called with a random column
    THEN it should return the 0 sport and ManualException with code 400
    """
    try:
        _ = sport_service.find(junk=generate_uuid())
    except ManualException as ex:
        assert ex.code == 400


def test_sport_find_by_non_existent_include():
    """
    GIVEN 2 sport instance in the database
    WHEN the find method is called with a random include
    THEN it should return the 0 sport and ManualException with code 400
    """
    try:
        _ = sport_service.find(include=['junk'])
    except ManualException as ex:
        assert ex.code == 400


def test_sport_find_by_non_existent_expand():
    """
    GIVEN 2 sport instance in the database
    WHEN the find method is called with a random expand
    THEN it should return the 0 sport and ManualException with code 400
    """
    try:
        _ = sport_service.find(expand=['junk'])
    except ManualException as ex:
        assert ex.code == 400


###########
# Create
###########
def test_sport_create(reset_db, pause_notification):
    """
    GIVEN 0 sport instance in the database
    WHEN the create method is called
    THEN it should return 1 sport and add 1 sport instance into the database
    """

    sport = sport_service.create(name=pytest.sport_name)
    assert sport.uuid is not None
    assert sport.name is not None


def test_sport_create_dup_sport_name(pause_notification):
    """
    GIVEN 1 sport instance in the database
    WHEN the create method is called with duplicate sport_name
    THEN it should return 0 sport and add 0 sport instance into the database and ManualException with code 500
    """

    try:
        _ = sport_service.create(name=pytest.sport_name)
    except ManualException as ex:
        assert ex.code == 500


def test_sport_create_wo_sport_name(pause_notification):
    """
    GIVEN 1 sport instance in the database
    WHEN the create method is called without sport_name
    THEN it should return 0 sport and add 0 sport instance into the database and ManualException with code 500
    """

    try:
        _ = sport_service.create()
    except ManualException as ex:
        assert ex.code == 500


def test_sport_create_w_non_existent_name(pause_notification):
    """
    GIVEN 1 sport instance in the database
    WHEN the create method is called with non existent sport_name uuid
    THEN it should return 0 sport and add 0 sport instance into the database and ManualException with code 500
    """

    try:
        _ = sport_service.create(name=generate_uuid())
    except ManualException as ex:
        assert ex.code == 500


def test_sport_create_w_bad_field(reset_db, pause_notification):
    """
    GIVEN 0 sport instance in the database
    WHEN the create method is called with a non existent field
    THEN it should return 0 sport and add 0 sport instance into the database and ManualException with code 500
    """

    try:
        _ = sport_service.create(name=pytest.sport_name, junk='junk')
    except ManualException as ex:
        assert ex.code == 500


###########
# Misc
###########
def test_fetch_contest(reset_db, pause_notification, mock_fetch_contest, seed_sport):
    """
    GIVEN 2 sport instances in the database
    WHEN the fetch_contest method is called
    THEN it should return a contest
    """
    contest = sport_service.fetch_contest(uuid=str(pytest.contest_uuid), params=None)
    assert contest['uuid'] == str(pytest.contest_uuid)


def test_fetch_course(reset_db, pause_notification, mock_fetch_course, seed_sport):
    """
    GIVEN 2 sport instances in the database
    WHEN the fetch_course method is called
    THEN it should return a course
    """
    course = sport_service.fetch_course(uuid=str(pytest.location_uuid), params=None)
    assert course['uuid'] == str(pytest.location_uuid)


def test_fetch_score(reset_db, pause_notification, mock_fetch_score, seed_sport):
    """
    GIVEN 2 sport instances in the database
    WHEN the fetch_score method is called
    THEN it should return a score
    """
    score = sport_service.fetch_score(uuid=str(pytest.contest_uuid), params=None)
    assert score['uuid'] == str(pytest.score_uuid)


def test_update_score(reset_db, pause_notification, mock_update_score, seed_sport):
    """
    GIVEN 2 sport instances in the database
    WHEN the update_score method is called
    THEN it should return True
    """
    assert sport_service.update_score(uuid=str(pytest.contest_uuid), sheet=None)
