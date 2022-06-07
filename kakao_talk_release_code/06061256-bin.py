import csv
import time
import pymysql
import requests
from bs4 import BeautifulSoup

# 상위 2000 영화 div 추출

k = []
code_num = []

for page in range(1, 41):
    urls = f'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220604&page={page}'
    for j in range(2, 51):

        html = requests.get(urls)

        soup = BeautifulSoup(html.content, 'html.parser')

        title_url = soup.select_one(
            f'#old_content > table > tbody > tr:nth-child({j}) > td.title  ')
        if title_url == None:
            continue
        else:
            k.append(title_url)
            print("2000")

# 상위 2000개 영화 코드 번호 추출

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for i in range(0, len(k)):

    a = list(str(k[i]))

    for j in range(0, len(a) - 3):

        if a[j] == "c" and a[j + 1] == "o" and a[j + 2] == "d" and a[j + 3] == "e":
            if a[j + 11] == " ":
                code_num.append(int("".join(a[j + 5:j + 10])))
                break
            else:
                code_num.append(int("".join(a[j + 5:j + 11])))
                print("2000 code_num")
                break

# 관련 영화 코드 번호 추출

extra_code_num = []

for i in code_num:
    urls = f'https://movie.naver.com/movie/bi/mi/basic.naver?code={i}'
    for j in range(1, 6):
        html = requests.get(urls)
        soup = BeautifulSoup(html.content, 'html.parser')

        title_url = soup.select_one(
            f' #content > div.article > div:nth-child(7) > div:nth-child({j})  ')
        if title_url == None:
            continue
        else:
            extra_code_num.append(title_url)
            print("appending similar movie")

for i in range(0, len(extra_code_num)):
    print("chaging similar")

    a = list(str(extra_code_num[i]))

    for j in range(0, len(a) - 3):

        if a[j] == "c" and a[j + 1] == "o" and a[j + 2] == "d" and a[j + 3] == "e":
            if a[j + 11] == " " or a[j + 11] == "#" or a[j + 11] == "&":
                code_num.append(int("".join(a[j + 5:j + 10])))
                break
            elif a[j + 9] == " " or a[j + 9] == "#" or a[j + 9] == "&":
                code_num.append(int("".join(a[j + 5:j + 8])))
                break
            elif a[j + 10] == " " or a[j + 10] == "#" or a[j + 10] == "&":
                code_num.append(int("".join(a[j + 5:j + 9])))
                break
            else:
                code_num.append(int("".join(a[j + 5:j + 11])))
                break

code_num = set(code_num)
print(code_num)
print(len(code_num))



