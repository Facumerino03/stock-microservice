from marshmallow import Schema, fields, post_load # type: ignore
from app.models import Receipt

class ReceiptMap(Schema):
    id = fields.Integer(dump_only=True)
    date = fields.DateTime(required=True)
    id_header = fields.Integer(required=True)
    id_footer = fields.Integer(required=True)
    id_receipt_type = fields.Integer(required=True)
    receipt_type = fields.Nested('ReceiptTypeMap', dump_only=True)
    items = fields.Nested('ReceiptItemMap', many=True, dump_only=True)
    
    @post_load
    def make_receipt(self, data, **kwargs):
        return Receipt(**data)
