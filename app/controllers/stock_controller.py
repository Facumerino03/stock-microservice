from flask import Blueprint, request # type: ignore
from app.services import StockService
from app.mapping import StockMap
from app.mapping import MessageMap
from app.services import MessageBuilder

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stock/<int:id>', methods=['GET'])
def get(id: int):
    stock = StockService.find(id)
    stock_map = StockMap()
    stock_data = stock_map.dump(stock)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontró el stock').add_data({'stock': stock_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@stock_bp.route('/stocks', methods=['POST'])
def post():
    stock_map = StockMap()
    stock = stock_map.load(request.json)
    StockService.register(stock)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Stock creado').build()
    return message_map.dump(message_finish), 200


@stock_bp.route('/stocks/<int:id>', methods=['PUT'])
def put(id: int):
    stock_map = StockMap()
    new_stock = stock_map.load(request.json)
    new_stock.id = id
    StockService.save(new_stock)
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Stock actualizado').build()
    return message_map.dump(message_finish), 200