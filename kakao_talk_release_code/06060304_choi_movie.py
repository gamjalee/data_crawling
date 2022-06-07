import pymysql
import requests
from bs4 import BeautifulSoup

conn = pymysql.connect(host="localhost", user="root", password="1019", db="project", charset="utf8")
try:
    curs = conn.cursor()
    sql = """insert into movie(title, netizen_rate, audience_rate, review_count ,playing_time, opening_date, director, image, enter_date)
             values (%s, %s, %s, %s, %s, %s, %s, %s , %s, now())"""

    insert_data = []

    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=10016'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        #제목
        title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')
        title = title.text

        #제목(in English)
        title_English = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > strong')
        title_English = title_English.text

        index = title_English.find(',')
        title_English = title_English[0:index]

        #네티즌 평점

        netizen_rate = ""
        netizen_rates = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > div.main_score > div.score.score_left > div.star_score')
        tmp = netizen_rates.find_all('em')

        if netizen_rates is None:
            netizen_rate = None
        else:
            for i in tmp:
                tmp1 = i.text
                netizen_rate += tmp1

        netizen_rate.strip()
        netizen_rate = float(netizen_rate.strip())

        #관람객 평점

        audience_rate = ""
        audience_rates = soup.select_one('#actualPointPersentBasic > div')
        tmp = audience_rates.find_all('em')

        if audience_rates is None:
            audience_rate = 0.00
        else :
            for i in tmp:
                tmp1 = i.text
                audience_rate += tmp1

            # audience_rate = float(audience_rate)

        #리뷰 수
        review_count = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_total > strong > em')

        if review_count is None:
            review_count = None
            review_count2 =soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(4) > div:nth-child(2) > div.score_total > strong > em')
            if review_count2 is None:
                review_count = None
            else:
                review_count = review_count2.text.strip()
        else :
            review_count = review_count.text.strip()

        #상영시간
        playing_time = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')

        if playing_time is None:
            playing_time = None
        else:
            playing_time = playing_time.text


        #개봉날짜
        opening_year = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(1)')

        if opening_year is None:
            opening_year = None
        else:
            opening_year = opening_year.text.strip()

        opening_monthd = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(2)')

        if opening_monthd is None:
            opening_monthd = None
        else:
            opening_monthd =opening_monthd.text

        opening_date = opening_year + opening_monthd


        #director
        director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')

        if director is None:
            director = None
        else:
            director = director.text

        #image
        image = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a > img')

        if image is None:
            image = None
        else:
            image = image['src']

        #actor 배우
        actors_tmp = []
        actors = soup.select_one('#content > div.article > div.wide_info_area > div.mv_info > div.info_spec2 > dl.step2 > dd')

        if actors is None:
            actors_tmp = None
        else:
            tmp1 = ""
            tmp = actors.find_all('a')

            for i in tmp:
                tmp1 = i.text
                index = tmp1.find('(')

                tmp1 = tmp1[0:index]
                actors_tmp.append(tmp1)

        #장르
        genres_tmp = []
        genres = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')

        if genres is None:
            genres = None

        else:
            tmp1 = ""
            tmp = genres.find_all('a')

            for i in tmp:
                tmp1 = i.text
                genres_tmp.append(tmp1)

        #Famous_lines 명대사

        famous_lines_tmp = []
        famous_lines = soup.select('#content > div.article > div:nth-child(7) > div:nth-child(1) > div > ul > li')

        if famous_lines is None:
            famous_lines = None
        else:
            for line in famous_lines:
                tmp = line.select_one('div > div > strong')
                famous_lines_tmp.append(tmp.text)

        print(title)
        print(title_English)
        print(netizen_rate)
        print(audience_rate)
        print(review_count)
        print(playing_time)
        print(opening_date)
        print(director)
        print(image)
        print(actors_tmp)
        print(genres_tmp)
        print(famous_lines_tmp)

finally:
    conn.close()

