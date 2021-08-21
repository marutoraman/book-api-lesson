import os,sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from engine.book_scraping_ans import *


def run(keyword:str):
    pass
    
    
if __name__ == "__main__":
    if len(sys.argv) >= 1:
        keyword = sys.argv[1]
        run(keyword)