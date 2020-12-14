import logging

from .base import Base
from .sports import Golf as GolfService
from ..external import Contest as ContestExternal, Score as ScoreExternal, Course as CourseExternal
from ..models import Sport as SportModel


class Sport(Base):
    def __init__(self):
        Base.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.sport_model = SportModel
        self.contest_external = ContestExternal()
        self.score_external = ScoreExternal()
        self.course_external = CourseExternal()
        self.golf_service = GolfService()

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
            sport = sports.items[0]

            if sport.name == 'golf':
                # this will need to be changed to be more general and not just for golf
                location_res = self.course_external.get_course(uuid=contest['location_uuid'])
                location = location_res['data']['courses']

            participants = [participant['user_uuid'] for participant in contest['participants']]
            sheet = self.generate_sheet(name=sports.items[0].name, location=location, participants=participants)
            score_res = self.score_external.get_score(uuid=contest["uuid"])
            score_uuid = score_res['data']['scores']['uuid']
            _ = self.score_external.update_sheet(uuid=score_uuid, json={'sheet': sheet})

    def generate_sheet(self, name, location, participants):
        if name == 'golf':
            sheet = self.golf_service.transform_template(course=location, participants=participants)
        return sheet
