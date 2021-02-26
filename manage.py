import os

from flask.cli import FlaskGroup

from bin import init_sports
from src import app, db, cache

cli = FlaskGroup(app)


def full_load():
    os.system('flask seed run')
    init_sports()


def init_db():
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


def drop_db():
    db.drop_all()
    db.session.commit()


def configure_db():
    db.configure_mappers()
    db.session.commit()


def create_db():
    db.create_all()
    db.session.commit()


def reset_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


def clear_db():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()


def clear_cache():
    common.cache.clear()


def initialize_sports():
    init_sports()
    return


@cli.command("init")
def init():
    init_db()


@cli.command("load")
def load():
    full_load()


@cli.command("create")
def create():
    create_db()


@cli.command("drop")
def drop():
    drop_db()


@cli.command("reset")
def reset():
    reset_db()


@cli.command("configure")
def configure():
    configure_db()


@cli.command("delete")
def delete():
    clear_db()


@cli.command("flush_cache")
def flush_cache():
    clear_cache()


@cli.command("init_sport")
def init_sport():
    initialize_sports()


if __name__ == "__main__":
    cli()
