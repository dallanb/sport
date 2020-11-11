import logging

from src import db, Sport


def init_sports():
    logging.info(f"init_sports started")
    sports = ['golf']

    for sport_item in sports:
        sport = Sport(name=sport_item)
        db.session.add(sport)
    db.session.commit()
    logging.info(f"init_sports completed")
    return
