from engine.book_scraping import *

def test_book():
    res = BookScraping.fetch_books(keyword="Python",max_results=40,page_count=10)
    assert False