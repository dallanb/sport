import logging

from src import db, Sport


def init_sports():
    sports = ['golf']

    for sport_item in sports:
        sport = Sport(name=sport_item)
        db.session.add(sport)
    db.session.commit()
    return
