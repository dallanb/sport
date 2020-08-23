from .. import db
from .mixins import BaseMixin


class Sport(db.Model, BaseMixin):
    name = db.Column(db.String, unique=True, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


Sport.register()
