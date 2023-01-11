import pytest
from web_scraper.web_scraper import get_citations_needed_count, get_citations_needed_report

# @pytest.mark.skip("TODO")
def test_sign_of_life_count():
    assert get_citations_needed_count

# @pytest.mark.skip("TODO")
def test_sign_of_life_report():
    assert get_citations_needed_report

# @pytest.mark.skip("TODO")
def test_zero():
    url = 'https://en.wikipedia.org/wiki/Virtual_Boy'
    actual = get_citations_needed_count(url)
    expected = 0
    assert expected == actual

# @pytest.mark.skip("TODO")
def test_one():
    url = 'https://en.wikipedia.org/wiki/Nintendo_64'
    actual = get_citations_needed_count(url)
    expected = 1
    assert expected == actual

# @pytest.mark.skip("TODO")
def test_many():
    url = 'https://en.wikipedia.org/wiki/Quaternary_extinction_event'
    actual = get_citations_needed_count(url)
    expected = 8
    assert expected == actual

@pytest.mark.skip("TODO")
def test_report():
    url = 'https://en.wikipedia.org/wiki/Quaternary_extinction_event'
    actual = get_citations_needed_report(url)
    expected = 8
    assert expected == actual