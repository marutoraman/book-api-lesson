from engine.book_scraping_ans import *

def test_book():
    res = BookScraping.fetch_books(keyword="Python",max_results=40,page_count=10)
    if not res or len(res) == 0:
        assert False
    assert res[0].title