import requests
from bs4 import BeautifulSoup



def get_review_url(code):
    #https://movie.naver.com/movie/bi/mi/reviewread.naver?nid=4807776&code=192608&order=#tab
    #영화 설명-리뷰 페이지에서 위 url의 nid 3개 받아오는 코드
    url = f'https://movie.naver.com/movie/bi/mi/review.naver?code={code}'
    response = requests.get(url)
    review_num = []
    insert_data = []
    review_name = []
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        url_test = soup.select_one(
            f' #reviewTab > div > div > ul ')
        if url_test == None:
            return []
        for i in range(1,4):
            review_url=soup.select_one(
                f' #reviewTab > div > div > ul > li:nth-child({i}) > a ')

            if review_url == None:
                continue
            else:
                insert_data.append(review_url)
                #print(review_url)
                review_name.append(review_url.text)
                #print(review_name)

        for j in range(0, len(insert_data)):
            #print("director code extract")
            a=list(str(insert_data[j]))
            #print(a)

            for k in range(0, len(a)-3):
                if a[k] == "D" and a[k + 1] == "e" and a[k + 2] == "t" and a[k + 3] == "a" and a[k + 4] == "i" and a[k + 5] == "l" and a[k + 6] == "(":
                    if  a[k + 8] == ")":
                        #code가 1자리
                        review_num.append(int("".join(a[k + 7:k + 8])))
                        #print(a[k + 7:k + 8])
                        break
                    elif  a[k + 9] == ")":
                        #code가 2자리
                        review_num.append(int("".join(a[k + 7:k + 9])))
                        #print(a[k + 7:k + 9])
                        break
                    elif a[k + 10] == ")":
                        #code가 3자리
                        review_num.append(int("".join(a[k + 7:k + 10])))
                        #print(a[k + 7:k + 10])
                        break
                    elif a[k + 11] == ")":
                        #code가 4자리
                        review_num.append(int("".join(a[k + 7:k + 11])))
                        #print(a[k + 7:k + 11])
                        break
                    elif a[k + 12] == ")":
                        #code가 5자리
                        review_num.append(int("".join(a[k + 7:k + 12])))
                        #print(a[k + 7:k + 12])
                        break
                    elif a[k + 13] == ")":
                        #code가 6자리
                        review_num.append(int("".join(a[k + 7:k + 13])))
                        #print(a[k + 7:k + 13])
                        break
                    elif a[k + 14] == ")":
                        #code가 7자리
                        review_num.append(int("".join(a[k + 7:k + 14])))
                        #print(a[k + 7:k + 14])
                        break
                    elif a[k + 15] == ")":
                        #code가 8자리
                        review_num.append(int("".join(a[k + 7:k + 15])))
                        #print(a[k + 7:k + 15])
                        break
                    elif  a[k + 16] == ")":
                        # code가 9자리
                        review_num.append(int("".join(a[k + 7:k + 16])))
                        #print(a[k + 7:k + 16])
                        break
                    else:
                        # else 이외에 그냥 없는걸로
                        print("%d num is not exist" %code)
                        break


    review_num=set(review_num)
    review_num=list(review_num)
    #print(review_num)
    #print(review_name)
    #print(len(review_num))
    return review_num


def code_to_get_review(code_movies):
    #인자로 영화들의 code list를 주면
    review_nums = []
    for code_movie in code_movies:
        get_url = get_review_url(code_movie)
        for aa in get_url:
            review_nums.append(aa)
        # print(type(get_director_url(url)))

    #print("direc_nums")
    #print(review_nums)
    return review_nums


#get_review_url(192608)
print(code_to_get_review([192608]))

#print(insert_data)
