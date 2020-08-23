from flask import g
import logging


def init_sports():
    logging.info(f"init_sports started")
    sports = ['golf']
    Sport = g.src.Sport

    for sport_item in sports:
        sport = Sport(name=sport_item)
        g.src.db.session.add(sport)
    g.src.db.session.commit()
    logging.info(f"init_sports completed")
    return
