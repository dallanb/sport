from .. import app

from . import Base


class Score(Base):
    def __init__(self):
        Base.__init__(self)
        self.base_url = app.config['SCORE_URL']

    def get_score(self, uuid, params=None):
        url = f'{self.base_url}/scores/contest/{uuid}'
        res = self.get(url=url, params=params)
        return res.json()

    def update_sheet(self, uuid, json):
        url = f'{self.base_url}/scores/{uuid}'
        res = self.put(url=url, json=json)
        return res.json()
