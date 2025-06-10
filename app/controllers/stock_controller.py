import logging
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


@stock_bp.route('/stocks', methods=['GET'])
def get_all():
    stocks = StockService.find_all()
    stock_map = StockMap()
    stocks_data = stock_map.dump(stocks, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Se encontraron todos los stocks').add_data({'stocks': stocks_data}).build()
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


@stock_bp.route('/stocks/calculate/<int:article_id>', methods=['GET'])
def calculate_stock(article_id: int):
    total_stock = StockService.calculate_stock(article_id)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Stock calculado').add_data({'article_id': article_id, 'total_stock': total_stock}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200


@stock_bp.route('/stocks/by', methods=['GET'])
def find_by():
    kwargs = request.args.to_dict()
    stocks = StockService.find_by(**kwargs)
    stock_map = StockMap()
    stocks_data = stock_map.dump(stocks, many=True)
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message('Stocks encontrados por filtros').add_data({'stocks': stocks_data}).build()
    message_map = MessageMap()
    return message_map.dump(message_finish), 200