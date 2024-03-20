from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    username = fields.String()
    email = fields.String()
    join_date = fields.Date(dump_only=True)


class NotesSchema(Schema):
    id = fields.Integer(dump_only=True)
    data=fields.String()
    date=fields.DateTime(dump_only=True)
    user_id=fields.Integer(load_only=True)
