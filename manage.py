import os
from flask import g
from flask.cli import FlaskGroup
from src import app, db, cache
from bin import init_sports
import src

cli = FlaskGroup(app)


def full_init():
    initialize_sports()
    os.system('flask seed run')


def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


def clear_db():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()


def clear_cache():
    cache.clear()


def initialize_sports():
    with app.app_context():
        g.src = src
        init_sports()
        return


@cli.command("init")
def init():
    full_init()


@cli.command("reset_db")
def reset_db():
    create_db()


@cli.command("delete_db")
def delete_db():
    clear_db()


@cli.command("flush_cache")
def flush_cache():
    clear_cache()


@cli.command("init_sport")
def init_sport():
    initialize_sports()


if __name__ == "__main__":
    cli()
