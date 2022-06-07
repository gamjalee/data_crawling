import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(host="localhost", user="root", password="1019", db="project", charset="utf8")
try:
    curs = conn.cursor()
    sql = """insert into movie(name_korean, name_english, work, enter_date)
             values (%s, %s , %s, now())"""

    insert_data = []

    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=187347'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        actors = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(2) > div > ul > li')

        for actor in actors:
            actor_name = actor.select_one('a.tx_people')

            if actor_name is None:
                actor_name = None
            else:
                actor_name = actor_name.text.strip()


            role = actor.select_one('dl > dt')

            if role is None:
                role = None
            else:
                role = role.text.strip()

            casting_name = actor.select_one('dl > dd')

            if casting_name is None:
                casting_name = None
            else:
                casting_name = casting_name.text.replace('역','').strip()

            print(actor_name)
            print(role)
            print(casting_name)


finally:
    conn.close()