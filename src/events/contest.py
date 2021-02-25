import logging

from src import ManualException
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
            contest = self.sport_service.fetch_contest(uuid=data['uuid'],
                                                       params={'expand': 'sport', 'include': 'participants'})

            if contest is None:
                raise ManualException(err=f'contest with uuid: {data["uuid"]} not found')

            sports = self.sport_service.find(uuid=contest['sport']['sport_uuid'])
            sport = sports.items[0]

            if sport.name == 'golf':
                # this will need to be changed to be more general and not just for golf
                location = self.sport_service.fetch_course(uuid=contest['location_uuid'])

            if location is None:
                raise ManualException(err=f'location with uuid: {contest["location_uuid"]} not found')

            participants = [participant['member_uuid'] for participant in contest['participants']]
            sheet = self.sport_service.generate_sheet(name=sports.items[0].name, location=location,
                                                      participants=participants)
            score = self.sport_service.fetch_score(uuid=contest["uuid"])
            if score is None:
                raise ManualException(err=f'score with uuid: {contest["uuid"]} not found')

            score_uuid = score['uuid']
            res = self.sport_service.update_score(uuid=score_uuid, sheet=sheet)
            if res is None:
                raise ManualException(err=f'score with uuid: {score_uuid} failed to update')
