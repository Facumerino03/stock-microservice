from marshmallow import Schema, fields, post_load #type: ignore
from app.models import Stock

class StockMap(Schema):

    id: int = fields.Integer(dump_only=True)
    id_article: int = fields.Integer(required=True)
    id_receipt: int = fields.Integer(required=True)
    quantity: int = fields.Integer(required=True)
    id_batch: int = fields.Integer(required=True)
    article = fields.Nested('ArticleMap', dump_only=True)
    batch = fields.Nested('BatchMap', dump_only=True)
    receipt = fields.Nested('ReceiptMap', dump_only=True)

    @post_load
    def bind_stock(self, data, **kwargs):
        return Stock(**data)