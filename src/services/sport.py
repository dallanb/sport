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
        return self._find(model=self.sport_model, **kwargs)

    def create(self, **kwargs):
        sport = self._init(model=self.sport_model, **kwargs)
        return self._save(instance=sport)

    def generate_sheet(self, name, location, participants):
        if name == 'golf':
            sheet = self.golf_service.transform_template(course=location, participants=participants)
        return sheet

    def fetch_contest(self, uuid, params=None):
        try:
            res = self.contest_external.get_contest(uuid=uuid,
                                                    params=params)
            contest = res['data']['contests']
            return contest
        except TypeError:
            self.logger.error('Contest fetch error')
            return None

    def fetch_course(self, uuid, params=None):
        try:
            res = self.course_external.get_course(uuid=uuid,
                                                  params=params)
            course = res['data']['courses']
            return course
        except TypeError:
            self.logger.error('Course fetch error')
            return None

    def fetch_score(self, uuid, params=None):
        try:
            res = self.score_external.get_score(uuid=uuid,
                                                params=params)
            score = res['data']['scores']
            return score
        except TypeError:
            self.logger.error('Score fetch error')
            return None

    def update_score(self, uuid, sheet):
        try:
            _ = self.score_external.update_sheet(uuid=uuid, json={'sheet': sheet})
            return True
        except TypeError:
            self.logger.error('Score update error')
            return None
