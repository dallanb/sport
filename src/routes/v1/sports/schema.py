from marshmallow import validate, Schema, post_dump
from webargs import fields


class DumpSportSchema(Schema):
    uuid = fields.UUID()
    ctime = fields.Integer()
    mtime = fields.Integer()
    name = fields.String()

    def get_attribute(self, obj, attr, default):
        return getattr(obj, attr, default)

    @post_dump
    def make_obj(self, data, **kwargs):
        return data


class FetchAllSportSchema(Schema):
    page = fields.Int(required=False, missing=1)
    per_page = fields.Int(required=False, missing=10)
    name = fields.String(required=False)


dump_schema = DumpSportSchema()
dump_many_schema = DumpSportSchema(many=True)
fetch_all_schema = FetchAllSportSchema()
