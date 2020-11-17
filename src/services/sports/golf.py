import pandas as pd

from src.common import get_sport_template, generate_uuid


class Golf:
    def __init__(self):
        self.name = 'golf'

    def transform_template(self, course, participants):
        template = get_sport_template(self.name)
        hole_df = pd.DataFrame(course['holes'])
        hole_df['strokes'] = None
        holes = hole_df.drop(columns=['ctime', 'mtime', 'course_uuid']).set_index('number').T.to_dict()
        sheet = []
        for participant in participants:
            sheet.append({**template})
            sheet[len(sheet) - 1]['uuid'] = str(generate_uuid())
            sheet[len(sheet) - 1]['participant'] = participant
            sheet[len(sheet) - 1]['holes'] = holes
        return sheet
