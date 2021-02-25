import logging
from src.external import Contest as ContestExternal, Course as CourseExternal, Score as ScoreExternal
from src.services import SportService


class Contest:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.contest_external = ContestExternal()
        self.course_external = CourseExternal()
        self.score_external = ScoreExternal()
        self.sport_service = SportService()

    def handle_event(self, key, data):
        if key == 'contest_ready':
            # create a score log
            contest_res = self.contest_external.get_contest(uuid=data['uuid'],
                                                            params={'expand': 'sport', 'include': 'participants'})
            contest = contest_res['data']['contests']
            sports = self.sport_service.find(uuid=contest['sport']['sport_uuid'])
            sport = sports.items[0]

            if sport.name == 'golf':
                # this will need to be changed to be more general and not just for golf
                location_res = self.course_external.get_course(uuid=contest['location_uuid'])
                location = location_res['data']['courses']

            participants = [participant['member_uuid'] for participant in contest['participants']]
            sheet = self.sport_service.generate_sheet(name=sports.items[0].name, location=location,
                                                      participants=participants)
            score_res = self.score_external.get_score(uuid=contest["uuid"])
            score_uuid = score_res['data']['scores']['uuid']
            _ = self.score_external.update_sheet(uuid=score_uuid, json={'sheet': sheet})
