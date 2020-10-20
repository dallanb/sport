import logging
from .base import Base
from ..external import Contest as ContestExternal, Score as ScoreExternal
from ..models import Sport as SportModel
from ..common.utils import get_sport_template


class Sport(Base):
    def __init__(self):
        Base.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.sport_model = SportModel
        self.contest_external = ContestExternal()
        self.score_external = ScoreExternal()

    def find(self, **kwargs):
        return Base.find(self, model=self.sport_model, **kwargs)

    def create(self, **kwargs):
        sport = self.init(model=self.sport_model, **kwargs)
        return self.save(instance=sport)

    def handle_event(self, key, data):
        if key == 'contest_ready':
            # create a score log
            contest_res = self.contest_external.get_contest(uuid=data['uuid'],
                                                            params={'expand': 'sport', 'include': 'participants'})
            contest = contest_res['data']['contests']
            sports = self.find(uuid=contest['sport']['sport_uuid'])
            participants = [participant['user_uuid'] for participant in contest['participants']]
            sheet = self.generate_sheet(name=sports.items[0].name, participants=participants)
            score_res = self.score_external.get_score(uuid=contest["uuid"])
            score_uuid = score_res['data']['scores']['uuid']
            _ = self.score_external.create_log(uuid=score_uuid, json={'sheet': sheet})

    @staticmethod
    def generate_sheet(name, participants):
        template = get_sport_template(name)
        sheet = []
        for participant in participants:
            sheet.append({**template})
            sheet[len(sheet) - 1]['participant'] = participant
        return sheet
