from marshmallow import Schema,fields # type: ignore

class MessageMap(Schema):

    message:str = fields.String(required=True, dump_only=True)
    code:str = fields.String(required=False, dump_only=True)
    data:str = fields.Dict(required=False, dump_only=True)