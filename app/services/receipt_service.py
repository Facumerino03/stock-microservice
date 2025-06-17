from app.models import Receipt
from typing import List
import requests # type: ignore 
from app.mapping import ReceiptMap
from app import cache
from tenacity import retry, wait_random, stop_after_attempt # type: ignore
import os

class ReceiptService():

    @staticmethod
    @retry(wait=wait_random(min=1, max=3), stop=stop_after_attempt(3))
    def find(id: int) -> 'Receipt':
        URL_RECEIPT_SERVICE = os.getenv('URL_RECEIPT_SERVICE')
        if not URL_RECEIPT_SERVICE:
            raise ValueError("Environment variable 'URL_RECEIPT_SERVICE' is not set.")
        
        result = cache.get(f'receipts_{id}')
        if result is None:  
            receipt_mapping = ReceiptMap()
            receipt_r = requests.get(f"{URL_RECEIPT_SERVICE}/receipts/{id}", verify=False)
            if receipt_r.status_code == 200:
                result = receipt_mapping.load(receipt_r.json())
                cache.set(f'receipts_{id}', result, timeout=15)   
            else:
                raise Exception(f"Error fetching receipt with id {id}: {receipt_r.status_code} - {receipt_r.text}")
        return result