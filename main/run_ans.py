import os,sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.book_scraping_ans import *


def run(keyword:str):
    items = BookScraping.fetch_books(keyword=keyword,max_results=40,page_count=10)
    df = pd.DataFrame()
    for item in items:
        df = df.append(item.__dict__, ignore_index=True)
    df.to_csv("export.csv", encoding="utf-8_sig")
    
    
if __name__ == "__main__":
    if len(sys.argv) >= 1:
        keyword = sys.argv[1]
        run(keyword)