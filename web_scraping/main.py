"""
Web Scraping with Python using requests and bs4(BeautifulSoup)

Web Scraping = search for data on the internet and extract it
to use in your code.

requests = load data to your code.

bs4.BeautifulSoup = interpret HTML data in Python objects.

Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
"""
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='UTF-8')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(p.text)
