import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.book_scraping import *


def run(keyword:str):
    BookScraping.fetch_books(keyword=keyword,max_results=40,page_count=10)


if __name__ == "__main__":
    if len(sys.argv) >= 1:
        keyword = sys.argv[1]
        run(keyword)