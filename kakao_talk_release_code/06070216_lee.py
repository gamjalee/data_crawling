#https://movie.naver.com/movie/bi/mi/reviewread.naver?nid=4733712&code=191613&order=#tab
import requests
from bs4 import BeautifulSoup

def review(code):
    #https://movie.naver.com/movie/bi/mi/reviewread.naver?nid=4807776&code=192608&order=#tab
    #영화 설명-리뷰 페이지에서 위 url의 nid 3개 받아오는 코드
    url = f'https://movie.naver.com/movie/bi/mi/review.naver?code={code}'
    response = requests.get(url)

    review_username = []
    review_date = []
    review_good_1 = []
    review_good_2 = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        url_test = soup.select_one(
            f' #reviewTab > div > div > ul ')
        if url_test == None:
            #print("good")
            return []
        for i in range(1,4):
            uname=soup.select_one(
                f' #reviewTab > div > div > ul > li:nth-child({i}) > span > a ')
            date = soup.select_one(
                f' #reviewTab > div > div > ul > li:nth-child({i}) > span > em:nth-child(2) ')
            good = soup.select_one(
                f' #reviewTab > div > div > ul > li:nth-child({i}) > span > em:nth-child(3) ')
            if uname == None or date==None or good == None:
                continue
            else:
                review_username.append(uname.get_text())
                review_date.append(date.get_text())
                review_good_1.append(good.text)

        for j in range(0, len(review_good_1)):
            a=list(str(review_good_1[j]))
            for k in range(0, len(a)-3):
                if a[k] == "추" and a[k + 1] == "천" and a[k + 2] == " ":
                    review_good_2.append(int("".join(a[k + 2:])))
                    break
                else: # else 이외에 그냥 없는걸로
                    print("%d num is not exist" %code)
                    break

    print(review_username)
    print(review_date)
    print(review_good_2)

    return review_username

print(review(171539))