import csv
import time
import pymysql
import requests
from bs4 import BeautifulSoup

code_num = []
review_title = []
review_text = []

for i in code_num:
    urls = f'https://movie.naver.com/movie/bi/mi/review.naver?code={i}'
    html = requests.get(urls)
    soup = BeautifulSoup(html.content, 'html.parser')

    for j in range(1,4):
        title = soup.select_one(f'#reviewTab > div > div > ul > li:nth-child({j}) > a > strong')
        text = soup.select_one(f'#reviewTab > div > div > ul > li:nth-child({j}) > p > a')

        if title == None:
            continue
        else:
            review_title.append(title.get_text())

        if text == None:
            continue
        else:
            review_text.append(text.get_text())