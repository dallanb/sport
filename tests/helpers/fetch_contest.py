from uuid import uuid4

import pytest


def fetch_contest(self, uuid, params):
    if uuid == str(pytest.contest_uuid):
        return {
            'league_uuid': str(pytest.league_uuid),
            'location_uuid': str(pytest.location_uuid),
            'name': 'Super Contest',
            'uuid': uuid,
            'status': 'completed',
            'participants': [
                {
                    'member_uuid': str(pytest.member_uuid),
                    'uuid': str(uuid4())
                },
                {
                    'member_uuid': str(pytest.other_member_uuid),
                    'uuid': str(uuid4())
                }
            ],
            'sport': {
                'sport_uuid': str(pytest.sport.uuid),
                'uuid': str(uuid4())
            }
        }
    else:
        return None
