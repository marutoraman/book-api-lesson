import os
import requests
import re
import time
from common.utility import *

from models.book_item_ans import *

GOOGLE_BOOK_SEARCH_API = "https://www.googleapis.com/books/v1/volumes"

class BookScraping():
    
    @staticmethod
    def fetch_books(keyword:str, max_results:int, page_count:int=1):
        item_list=[]
        params = {
            "q":keyword,
            "maxResults":max_results,
        }
        item_list = []
        for page in range(page_count):
            params["startIndex"] = page * max_results
            res = requests.get(GOOGLE_BOOK_SEARCH_API,params=params)
            if res.status_code > 300:
                return item_list
            
            data = res.json()
            if not data.get("items"):
                return False
            for item in data.get("items"):
                try:
                    title = item["volumeInfo"]["title"]
                except:
                    title = ""
                try:
                    identifier = item["volumeInfo"]["industryIdentifiers"][0]["identifier"]
                except:
                    identifier = ""
                try:
                    description = item["volumeInfo"]["description"]
                except:
                    description = ""
                try:
                    authors = item["volumeInfo"]["authors"][0]
                except:
                    authors = ""
                print(title)
                item_list.append(
                        BookItem(title=title, isbn=identifier, description=description, author=authors, jan="")
                    )

            
        return item_list
    
                