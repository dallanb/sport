from flask import request
from flask_restful import marshal_with
from .schema import *
from ..base import Base
from ....common.response import DataResponse
from ....services import Sport


class SportsAPI(Base):
    def __init__(self):
        Base.__init__(self)
        self.sport = Sport()

    @marshal_with(DataResponse.marshallable())
    def get(self, uuid):
        sports = self.sport.find(uuid=uuid)
        if not sports.total:
            self.throw_error(http_code=self.code.NOT_FOUND)
        return DataResponse(
            data={
                'sports': self.dump(
                    schema=dump_schema,
                    instance=sports.items[0]
                )
            }
        )


class SportsListAPI(Base):
    def __init__(self):
        Base.__init__(self)
        self.sport = Sport()

    @marshal_with(DataResponse.marshallable())
    def get(self):
        data = self.clean(schema=fetch_all_schema, instance=request.args)
        sports = self.sport.find(**data)
        return DataResponse(
            data={
                '_metadata': self.prepare_metadata(
                    total_count=sports.total,
                    page_count=len(sports.items),
                    page=data['page'],
                    per_page=data['per_page']),
                'sports': self.dump(
                    schema=dump_many_schema,
                    instance=sports.items
                )
            }
        )
