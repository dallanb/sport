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
