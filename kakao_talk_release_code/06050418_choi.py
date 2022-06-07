import pymysql
import requests
from bs4 import BeautifulSoup

#conn = pymysql.connect(host="localhost", user="root", password="1019", db="project", charset="utf8")
#try:
    #curs = conn.cursor()
    #sql = """insert into movie(title, netizen_rate, audience_rate, review_count ,playing_time, opening_date, director, image, enter_date)
    #         values (%s, %s, %s, %s, %s, %s, %s, %s , %s, now())"""

insert_data = []


url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=69956'

response = requests.get(url)
# content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')


        #제목
    title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a')

        #네티즌 평점
    netizen_rate1 = soup.select_one('#pointNetizenPersentBasic > em.num7')
    netizen_rate2 = soup.select_one('#pointNetizenPersentBasic > em.num6')
    netizen_rate3 = soup.select_one('#pointNetizenPersentBasic > em.num9')

    netizen_rate = netizen_rate1.text + '.' + netizen_rate2.text + netizen_rate3.text

        #관람객 평점
    audience_rate1 = soup.select_one('#actualPointPersentBasic > div > em.num8')
    audience_rate2 = soup.select_one('#actualPointPersentBasic > div > em.num1')
    audience_rate3 = soup.select_one('#actualPointPersentBasic > div > em.num2')

    audience_rate =audience_rate1.text + '.' + audience_rate2.text + audience_rate3.text

        #리뷰 수
    review_count = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_total > strong > em')
    review_count = review_count.text.strip()

        #상영시간
    playing_time = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)')
    playing_time =playing_time.text


        #개봉날짜
    opening_year = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(1)')
    opening_year = opening_year.text.strip()

    opening_monthd = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4) > a:nth-child(2)')
    opening_monthd =opening_monthd.text

    opening_date = opening_year + opening_monthd


        #director
    director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')
    director = director.text

        #image
    image = soup.select_one('#content > div.article > div.mv_info_area > div.poster > a > img')
    image = image['src']

        #actor 배우
    actors_tmp = []
    actors = soup.select('#content > div.article > div.wide_info_area > div.mv_info > div.info_spec2 > dl.step2 > dd')

    for actor in actors:
        actor = actor.select_one('a:nth-child(n)')
        actor = actor.text
        actors_tmp.append(actor)
        print(actor)

        #장르

        # genres = soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1)')
        #
        # for genre in genres:
        #     genre =  genre.select()

    print(actors_tmp)
    print(title.text)
    print(netizen_rate)
    print(audience_rate)
    print(review_count)
    print(playing_time)
    print(opening_date)
    print(director)
    print(image)







#finally:#conn.close()