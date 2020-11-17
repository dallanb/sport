import os
import json
import uuid as UUID
from time import time


def generate_hash(items):
    frozen = frozenset(items)
    return hash(frozen)


def time_now():
    return int(time() * 1000.0)


def add_years(t, years=0):
    return t + 31104000000 * years


def generate_uuid():
    return UUID.uuid4()


def camel_to_snake(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')


def get_sport_template_path(sport):
    return os.path.join('src', 'templates', sport, 'data_model.json')


def get_sport_template(sport):
    with open(os.path.join('src', 'templates', sport, 'data_model.json')) as f:
        return json.load(f)
