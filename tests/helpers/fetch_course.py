from uuid import uuid4

import pytest


def fetch_course(self, uuid, params=None):
    if uuid == str(pytest.location_uuid):
        return {
            "name": "Northlands Golf Course",
            "uuid": str(pytest.location_uuid),
            "status": "pending",
            "city": "North Vancouver",
            "province": "British Columbia",
            "line_1": "3400 Anne Macdonald Way",
            "country": "CA",
            "holes": [
                {
                    "name": "Uno",
                    "uuid": str(uuid4()),
                    "ctime": 1608417460962,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 1,
                    "distance": 424,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417489012,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 2,
                    "distance": 353,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417500287,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 3,
                    "distance": 177,
                    "par": 3
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417533077,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 4,
                    "distance": 558,
                    "par": 5
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417549518,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 5,
                    "distance": 434,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417556525,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 6,
                    "distance": 368,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417562791,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 7,
                    "distance": 401,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417568989,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 8,
                    "distance": 220,
                    "par": 3
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417577904,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 9,
                    "distance": 419,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417585551,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 10,
                    "distance": 337,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417591552,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 11,
                    "distance": 412,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417597614,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 12,
                    "distance": 190,
                    "par": 3
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417603809,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 13,
                    "distance": 322,
                    "par": 4
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417609323,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 14,
                    "distance": 194,
                    "par": 3
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417615227,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 15,
                    "distance": 547,
                    "par": 5
                },
                {
                    "name": None,
                    "uuid": "324261d8-1fff-4bcb-8698-0cd458514627",
                    "ctime": 1608417620843,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 16,
                    "distance": 168,
                    "par": 3
                },
                {
                    "name": None,
                    "uuid": str(uuid4()),
                    "ctime": 1608417627294,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 17,
                    "distance": 491,
                    "par": 5
                },
                {
                    "name": "Fin",
                    "uuid": str(uuid4()),
                    "ctime": 1608417641454,
                    "mtime": None,
                    "course_uuid": str(pytest.location_uuid),
                    "number": 18,
                    "distance": 508,
                    "par": 5
                }
            ]
        }
