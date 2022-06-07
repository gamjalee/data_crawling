import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(host="localhost", user="root", password="1019", db="project", charset="utf8")
try:
    curs = conn.cursor()
    sql = """insert into movie(name_korean, name_english, work, enter_date)
             values (%s, %s , %s, now())"""

    insert_data = []

    url = 'https://movie.naver.com/movie/bi/pi/basic.naver?code=301342'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        name_korean = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > h3 > a')

        if name_korean is None:
            name_korean = None
        else:
            name_korean = name_korean.text.strip()

        name_english = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info.character > strong')

        if name_english is None:
            name_english = None
        else:
            name_english = name_english.text.strip()

        works_tmp = []
        works = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(2) > div > ul > li')

        if works is None:
            works_tmp = None
        else:
            for work in works:
                tmp = work.select_one('div > strong > a')
                works_tmp.append(tmp.text.strip())

        print(name_korean)
        print(name_english)
        print(works_tmp)


finally:
    conn.close()