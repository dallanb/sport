from uuid import uuid4

import pytest


def fetch_score(self, uuid, params=None):
    if uuid == str(pytest.contest_uuid):
        return {
            "sheet": [
                {
                    "uuid": str(uuid4()),
                    "participant": str(pytest.member_uuid),
                    "handicap": None,
                    "status": "pending",
                    "holes": {
                        "1": {
                            "name": "Uno",
                            "uuid": str(uuid4()),
                            "distance": 424,
                            "par": 4,
                            "strokes": None
                        },
                        "2": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 353,
                            "par": 4,
                            "strokes": None
                        },
                        "3": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 177,
                            "par": 3,
                            "strokes": None
                        },
                        "4": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 558,
                            "par": 5,
                            "strokes": None
                        },
                        "5": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 434,
                            "par": 4,
                            "strokes": None
                        },
                        "6": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 368,
                            "par": 4,
                            "strokes": None
                        },
                        "7": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 401,
                            "par": 4,
                            "strokes": None
                        },
                        "8": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 220,
                            "par": 3,
                            "strokes": None
                        },
                        "9": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 419,
                            "par": 4,
                            "strokes": None
                        },
                        "10": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 337,
                            "par": 4,
                            "strokes": None
                        },
                        "11": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 412,
                            "par": 4,
                            "strokes": None
                        },
                        "12": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 190,
                            "par": 3,
                            "strokes": None
                        },
                        "13": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 322,
                            "par": 4,
                            "strokes": None
                        },
                        "14": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 194,
                            "par": 3,
                            "strokes": None
                        },
                        "15": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 547,
                            "par": 5,
                            "strokes": None
                        },
                        "16": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 168,
                            "par": 3,
                            "strokes": None
                        },
                        "17": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 491,
                            "par": 5,
                            "strokes": None
                        },
                        "18": {
                            "name": "Fin",
                            "uuid": str(uuid4()),
                            "distance": 508,
                            "par": 5,
                            "strokes": None
                        }
                    }
                },
                {
                    "uuid": str(uuid4()),
                    "participant": str(pytest.other_member_uuid),
                    "handicap": None,
                    "status": "pending",
                    "holes": {
                        "1": {
                            "name": "Uno",
                            "uuid": str(uuid4()),
                            "distance": 424,
                            "par": 4,
                            "strokes": None
                        },
                        "2": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 353,
                            "par": 4,
                            "strokes": None
                        },
                        "3": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 177,
                            "par": 3,
                            "strokes": None
                        },
                        "4": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 558,
                            "par": 5,
                            "strokes": None
                        },
                        "5": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 434,
                            "par": 4,
                            "strokes": None
                        },
                        "6": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 368,
                            "par": 4,
                            "strokes": None
                        },
                        "7": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 401,
                            "par": 4,
                            "strokes": None
                        },
                        "8": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 220,
                            "par": 3,
                            "strokes": None
                        },
                        "9": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 419,
                            "par": 4,
                            "strokes": None
                        },
                        "10": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 337,
                            "par": 4,
                            "strokes": None
                        },
                        "11": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 412,
                            "par": 4,
                            "strokes": None
                        },
                        "12": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 190,
                            "par": 3,
                            "strokes": None
                        },
                        "13": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 322,
                            "par": 4,
                            "strokes": None
                        },
                        "14": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 194,
                            "par": 3,
                            "strokes": None
                        },
                        "15": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 547,
                            "par": 5,
                            "strokes": None
                        },
                        "16": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 168,
                            "par": 3,
                            "strokes": None
                        },
                        "17": {
                            "name": None,
                            "uuid": str(uuid4()),
                            "distance": 491,
                            "par": 5,
                            "strokes": None
                        },
                        "18": {
                            "name": "Fin",
                            "uuid": str(uuid4()),
                            "distance": 508,
                            "par": 5,
                            "strokes": None
                        }
                    }
                },
            ],
            "_id": "601c5b84a0ac53001f9428e3",
            "contest_uuid": str(pytest.contest_uuid),
            "status": "active",
            "uuid": str(pytest.score_uuid),
            "ctime": "2021-02-04T20:39:32.691Z",
            "mtime": "2021-02-04T21:18:22.905Z",
            "__v": 0
        }
    else:
        return None
