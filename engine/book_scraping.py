import os
import requests
import re
import time
from common.utility import *

from models.book_item import *

GOOGLE_BOOK_SEARCH_API = "https://www.googleapis.com/books/v1/volumes"

class BookScraping():
    
    @staticmethod
    def fetch_books(keyword:str, max_results:int, page_count:int=1):
        pass    
                