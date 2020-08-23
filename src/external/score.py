from .. import app

from . import Base


class Score(Base):
    def __init__(self):
        Base.__init__(self)
        self.host = app.config['SCORE_HOST']
        self.port = app.config['SCORE_PORT']
        self.base_url = f'http://{self.host}:{self.port}'

    def get_contest(self, uuid, params=None):
        url = f'{self.base_url}/contests/{uuid}'
        res = self.get(url=url, params=params)
        return res.json()

    def get_contests(self, params=None):
        url = f'{self.base_url}/contests'
        res = self.get(url=url, params=params)
        return res.json()

    def create_log(self, uuid, json):
        url = f'{self.base_url}/scores/{uuid}/logs'
        res = self.post(url=url, json=json)
        return res.json()
