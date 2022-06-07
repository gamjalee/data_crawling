import requests
from bs4 import BeautifulSoup



def get_director_url(url):
    insert_data = []
    director_name = []
    direc_num = []
    #url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191613'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # director
        for i in range(1, 51):
            director_url = soup.select_one(
            f'#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a:nth-child({i})')
            if director_url == None:
                continue
            else:
                insert_data.append(director_url)
                director_name.append(director_url.text)

        for j in range(0, len(insert_data)):
            print("director code extract")
            a=list(str(insert_data[j]))

            for k in range(0, len(a)-3):
                if a[k] == "c" and a[k + 1] == "o" and a[k + 2] == "d" and a[k + 3] == "e":
                    if a[k + 11] == " ":
                        direc_num.append(int("".join(a[k + 5:k + 10])))
                        break
                    else:
                        direc_num.append(int("".join(a[k + 5:k + 11])))
                        print("2000 code_num")
                        break
    direc_num=set(direc_num)
    print(direc_num)
    print(director_name)
    print(len(direc_num))
    return direc_num