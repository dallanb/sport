import json

import pytest
from src import app, services


###########
# Fetch
###########


#############
# SUCCESS
#############

###########
# Fetch
###########
def test_fetch_sport(reset_db, pause_notification, seed_sport):
    """
    GIVEN a Flask application configured for testing
    WHEN the GET endpoint 'sport' is requested
    THEN check that the response is valid
    """
    sport_uuid = pytest.sport.uuid

    # Header
    headers = {'X-Consumer-Custom-ID': pytest.user_uuid}

    # Request
    response = app.test_client().get(f'/sports/{sport_uuid}', headers=headers)
    # Response
    assert response.status_code == 200
    response = json.loads(response.data)
    assert response['msg'] == "OK"
    sports = response['data']['sports']
    assert sports['uuid'] == str(sport_uuid)


###########
# Fetch All
###########
def test_fetch_all_sport():
    """
    GIVEN a Flask application configured for testing
    WHEN the GET endpoint 'sports' is requested
    THEN check that the response is valid
    """
    # Header
    headers = {'X-Consumer-Custom-ID': pytest.user_uuid}

    # Request
    response = app.test_client().get(f'/sports', headers=headers)
    # Response
    assert response.status_code == 200
    response = json.loads(response.data)
    assert response['msg'] == "OK"
    assert len(response['data']['sports']) == 2
    sports = response['data']['sports'][0]
    assert sports['uuid'] is not None
