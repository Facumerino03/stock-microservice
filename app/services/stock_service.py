from app.models import Stock, ReceiptItem, Receipt, ReceiptType
from app.repositories import StockRepository
from app.services import ArticleService, ReceiptService
from sqlalchemy import func #type: ignore
from app import db, cache
from tenacity import retry, wait_random, stop_after_attempt # type: ignore
import os

class StockService():

    @staticmethod
    @retry(wait=wait_random(min=1, max=3), stop=stop_after_attempt(3))
    def register(stock: Stock) -> Stock:
        try:
            article = ArticleService.find(stock.id_article)
        except Exception:
            raise ValueError(f"Article with ID {stock.id_article} does not exist.")

        try:
            receipt = ReceiptService.find(stock.id_receipt)
        except Exception:
            raise ValueError(f"Receipt with ID {stock.id_receipt} does not exist.")

        return StockRepository.save(stock)

    @staticmethod
    @retry(wait=wait_random(min=1, max=3), stop=stop_after_attempt(3))
    def calculate_stock(article_id: int) -> int:
        '''
        Calculate the total stock for a given article by summing the quantities from all receipts.
        :param article_id: ID of the article to calculate stock for.
        :return: Total stock quantity for the article.
        '''
        try:
            article = ArticleService.find(article_id)
        except Exception:
            raise ValueError(f"Article with ID {article_id} does not exist.")
        
        cache_key = f'stock_calculation_{article_id}'
        result = cache.get(cache_key)
        if result is not None:
            return result
    
        total_stock = db.session.query(
            func.sum(ReceiptItem.quantity * ReceiptType.type_entry)
        ).join(
            Receipt, ReceiptItem.id_receipt == Receipt.id
        ).join(
            ReceiptType, Receipt.id_receipt_type == ReceiptType.id
        ).filter(
            ReceiptItem.id_article == article_id
        ).scalar()
        
        result = total_stock if total_stock is not None else 0
        
        cache.set(cache_key, result, timeout=600)
        
        return result
    
    @staticmethod
    def save(stock: Stock) -> Stock:
        return StockRepository.save(stock)

    @staticmethod
    def find(id_stock: int) -> Stock:
        return StockRepository.find(id_stock)

    @staticmethod
    def find_all() -> list[Stock]:
        return StockRepository.find_all()

    @staticmethod
    def find_by(**kwargs) -> list[Stock]:
        return StockRepository.find_by(**kwargs)

