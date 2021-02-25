import pytest

from src.common import DB, Cleaner
from src.models import *
from tests.helpers import generate_uuid

db = DB()
cleaner = Cleaner()


def test_init(reset_db):
    """
    GIVEN a db instance
    WHEN calling the init method of the db instance on the Sport model
    THEN it should return the sport instance
    """
    instance = db.init(model=Sport, name=pytest.sport_name)
    assert cleaner.is_mapped(instance) == instance
    assert cleaner.is_uuid(instance.uuid) is not None
    assert instance.name == pytest.sport_name

    db.rollback()


def test_count():
    """
    GIVEN a db instance
    WHEN calling the count method of the db instance on the Sport model
    THEN it should return the number of sport instances
    """
    count = db.count(model=Sport)
    assert count == 1

    sport = db.init(model=Sport, name=pytest.sport_name)
    _ = db.save(instance=sport)
    count = db.count(model=Sport)
    assert count == 2


def test_add(reset_db):
    """
    GIVEN a db instance
    WHEN calling the add method of the db instance on a sport instance
    THEN it should add a sport instance to the database
    """
    instance = db.init(model=Sport, name=pytest.sport_name)
    sport = db.add(instance=instance)
    assert cleaner.is_uuid(sport.uuid) is not None
    assert sport.name == pytest.sport_name

    db.rollback()
    assert db.count(model=Sport) == 1


def test_commit(reset_db):
    """
    GIVEN a db instance
    WHEN calling the commit method of the db instance on a sport instance
    THEN it should add a sport instance to the database
    """
    instance = db.init(model=Sport, name=pytest.sport_name)
    sport = db.add(instance=instance)
    assert cleaner.is_uuid(sport.uuid) is not None
    assert sport.name == pytest.sport_name

    db.rollback()
    assert db.count(model=Sport) == 1

    _ = db.add(instance=instance)
    db.commit()
    assert db.count(model=Sport) == 2

    instance_0 = db.init(model=Sport, name='hockey')
    db.add(instance=instance_0)
    db.commit()
    assert db.count(model=Sport) == 3


def test_save(reset_db):
    """
    GIVEN a db instance
    WHEN calling the save method of the db instance on a sport instance
    THEN it should add a sport instance to the database
    """
    instance = db.init(model=Sport, name=pytest.sport_name)
    assert cleaner.is_uuid(instance.uuid) is not None
    assert instance.name == pytest.sport_name
    sport = db.save(instance=instance)
    assert db.count(model=Sport) == 2
    assert sport.name == pytest.sport_name


def test_find():
    """
    GIVEN a db instance
    WHEN calling the find method of the db instance
    THEN it should find a sport instance from the database
    """
    result = db.find(model=Sport)
    assert result.total == 2
    assert len(result.items) == 2

    result = db.find(model=Sport, uuid=generate_uuid())
    assert result.total == 0


def test_destroy():
    """
    GIVEN a db instance
    WHEN calling the destroy method of the db instance on a sport instance
    THEN it should remove the sport instance from the database
    """
    result = db.find(model=Sport)
    assert result.total == 2
    assert len(result.items) == 2
    instance = result.items[0]

    assert db.destroy(instance=instance)
    assert db.count(model=Sport) == 1


def test_rollback(reset_db):
    """
    GIVEN a db instance
    WHEN calling the rollback method of the db instance
    THEN it should rollback a sport instance from being inserted the database
    """
    instance = db.init(model=Sport, name=pytest.sport_name)
    db.rollback()
    db.commit()
    assert db.count(model=Sport) == 1

    instance = db.init(model=Sport, name=pytest.sport_name)
    db.save(instance=instance)
    db.rollback()
    assert db.count(model=Sport) == 2


def test_clean_query(reset_db):
    """
    GIVEN a db instance
    WHEN calling the clean_query method of the db instance
    THEN it should return a query
    """
    query = db.clean_query(model=Sport)
    assert query is not None


def test_run_query(reset_db, pause_notification, seed_sport):
    """
    GIVEN a db instance
    WHEN calling the run_query method of the db instance with a valid query
    THEN it should return the query result
    """
    query = db.clean_query(model=Sport)
    sports = db.run_query(query=query)
    assert sports.total == 2


def test_equal_filter():
    """
    GIVEN a db instance
    WHEN calling the find method of the db instance with an equal filter
    THEN it should return the query result
    """
    sports = db.find(model=Sport, name=pytest.sport_name)
    assert sports.total == 1

    sports = db.find(model=Sport, name=pytest.sport_name, uuid=pytest.sport.uuid)
    assert sports.items[0] == pytest.sport

# def test_nested_filter(reset_db, pause_notification, seed_member, seed_sport):
#     """
#     GIVEN a db instance
#     WHEN calling the find method of the db instance with a nested filter
#     THEN it should return the query result
#     """
#
#     services.SportService().apply(instance=pytest.member, sport=pytest.sport)
#
#     sports = db.find(model=Sport, nested={'member': {'uuid': pytest.member.uuid}})
#     assert sports.total == 1
#
#
# def test_within_filter():
#     """
#     GIVEN a db instance
#     WHEN calling the find method of the db instance with a within filter
#     THEN it should return the query result
#     """
#
#     sports = db.find(model=Sport)
#     assert sports.total == 1
#
#     sports = db.find(model=Sport, within={'uuid': [pytest.sport.uuid]})
#     assert sports.total == 1

# def test_has_key_filter():
#     """
#     GIVEN a db instance
#     WHEN calling the find method of the db instance with a has_key filter
#     THEN it should return the query result
#     """
#     
#
#     sports = db.find(model=Sport)
#     assert sports.total == 2
#
#     sports = db.find(model=Sport, has_key={'uuid': global_sport.uuid})
#     assert sports.total == 0
