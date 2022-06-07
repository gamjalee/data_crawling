import csv
import time
import pymysql
import requests
from bs4 import BeautifulSoup

f = open("C:/db/db.txt", 'w')
code_num = []
k = []
#old_content > ul > li:nth-child(1) > a
#old_content > ul > li:nth-child(20) > a

for page in range(53, 0, -1):
    urls = f'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2017&page={page}'
    for j in range(20, 0, -1):

        html = requests.get(urls)
        soup = BeautifulSoup(html.content, 'html.parser')
        title_url = soup.select_one(
            f' #old_content > ul > li:nth-child({j}) > a ')
        if title_url == None:
            continue
        else:
            a = list(str(title_url))
            for j in range(0, len(a)-3):

                if a[j] == "c" and a[j+1] == "o" and a[j+2] == "d" and a[j+3] == "e":
                    if a[j+10] == " " or a[j+10] == "#" or a[j+10] == "&":
                        f.write("".join(a[j+5:j+10]))
                        f.write(",")
                        break
                    elif a[j+9] == " " or a[j+9] == "#" or a[j+9] == "&":
                        f.write("".join(a[j+5:j+9]))
                        f.write(",")
                        break
                    elif a[j+10] == " " or a[j+10] == "#" or a[j+10] == "&":
                        f.write("".join(a[j+5:j+10]))
                        f.write(",")
                        break
                    else:
                        f.write("".join(a[j+5:j+10]))
                        f.write(",")
                        break