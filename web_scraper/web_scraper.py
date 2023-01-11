import pytest
from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    count = 0
    for element in soup.find_all(text='citation needed'):
        count += 1

    return count

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    report = ''
    for element in soup.find_all(text='citation needed'):
        passage = element.find_parents("a", limit=2)
        report += f'Citation needed for "{passage}"\n'

    return report

print(get_citations_needed_count('https://en.wikipedia.org/wiki/Virtual_Boy'))

print(get_citations_needed_report('https://en.wikipedia.org/wiki/Virtual_Boy'))

print(get_citations_needed_count('https://en.wikipedia.org/wiki/Nintendo_64'))

print(get_citations_needed_report('https://en.wikipedia.org/wiki/Nintendo_64'))

print(get_citations_needed_count('https://en.wikipedia.org/wiki/Quaternary_extinction_event'))

print(get_citations_needed_report('https://en.wikipedia.org/wiki/Quaternary_extinction_event'))