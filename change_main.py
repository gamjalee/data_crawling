import os
import pymysql


print("----------------------------------------------------------------")
print("")
print("            DataBase FinalProject _ 201811299 최범준 ")
print("")
print("----------------------------------------------------------------")
print("")

returnNum = 0

def open_db():
    conn = pymysql.connect(host="localhost", user="root", password="1019", db="final", charset="utf8")
    curs = conn.cursor(pymysql.cursors.DictCursor)

    return conn, curs

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    # now, to clear the screen : cls()


def orderBY():
    print(" 1. Year-to-year sorting(ORDERBY) \n 2. Open Date Sorting(ORDERBY)  \n 3. alphabetical order(ORDERBY)")
    print("")
    print("----------------------------------------------------------------")
    getnum = input()
    while(getnum != "1" and getnum != "2" and getnum != "3"):
        getnum = input()
        print("Enter again!")
    return getnum


def console():

    conn, cur = open_db()

    while True:
        # acls()
        print(" a. Search movie information \n b. Search an actor's film  \n c. Search a director's film \n d. Search movies with genre \n e. Search movies with opening date \n f. Search the actor in the movie \n g. Search the director who produced the movie \n h. Search the famous lines of the movie \n i. search the review of the movie \n q. exit")
        print("")
        print("----------------------------------------------------------------")

        temp = input()
        # 종료
        if temp == "q":
            cur.close()
            conn.close()
            break

        # 영화 제목 검색
        elif temp == "a":
            print("----------------------------------------------------------------")
            print("\n")
            returnNUM = orderBY()
            print(returnNUM)
            returnNUM = int(float(returnNUM))
            print("----------------------------------------------------------------\n")

            sql = ""

            title = input("Enter the movie title : ")

            if returnNUM == 1:
                sql = """select distinct *
                                from movie m
                                where m.title = '%s' order by m.enter_date;""" % (title)
            if returnNUM == 2:
                sql = """select distinct * from m.title = '%s' order by m.opening_date;""" % (title)
            if returnNUM == 3:
                sql = """select distinct * from m.title = '%s' order by m.title;""" % (title)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('movie code : %s, movie title(kor) : %s, movie title(eng) : %s, netizen rate : %s, audience rate : %s, review count : %s, running time : %s, Opening date: %s, image link : %s ' % (r['code_movie'], r['title'], r['title_English'], r['netizen_rate'], r['audience_rate'], r['review_count'], r['playing_time'], r['opening_date'], r['image']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")


        # 배우가 출연한 영화 검색
        elif temp == "b":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            returnNUM = int(float(returnNUM))
            print("----------------------------------------------------------------\n")
            sql = ""
            actor = input("Enter the actor name. : ")
            if returnNUM == 1:
                sql = """select distinct * from movie m, actor a where m.code_movie=a.code_movie and a.actor_name = '%s' group by m.code_movie order by m.enter_date;""" % (actor)
            if returnNUM == 2:
                sql = """select distinct * from movie m, actor a where m.code_movie=a.code_movie and a.actor_name = '%s' group by m.code_movie order by m.opening_date;""" % (actor)
            if returnNUM == 3:
                sql = """select distinct * from movie m, actor a where m.code_movie=a.code_movie and a.actor_name = '%s' group by m.code_movie order by m.title;""" % (actor)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('actor code : %s, movie code : %s, movie title(kor) : %s, name : %s, role : %s, casting name : %s ' % (
                    r['actor_code'], r['code_movie'], r['title'], r['actor_name'], r['role'], r['casting_name']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        # 감독이 제작한 영화 검색
        elif temp == "c":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            returnNUM = int(float(returnNUM))
            print("----------------------------------------------------------------\n")
            sql = ""
            director = input("Enter the director name. : ")
            if returnNUM == 1:
                sql = """select distinct * from movie m, director d where m.code_movie=d.code_movie and d.name_korean = '%s' group by m.code_movie order by m.enter_date;""" % (
                    director)
            if returnNUM == 2:
                sql = """select distinct * from movie m, director d where m.code_movie=d.code_movie and d.name_korean = '%s'  group by m.code_movie order by m.opening_date;""" % (
                    director)
            if returnNUM == 3:
                sql = """select distinct * from movie m, director d where m.code_movie=d.code_movie and d.name_korean = '%s' group by m.code_movie order by m.title;""" % (
                    director)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('director code : %s, movie code : %s, title : %s , name(kor) : %s, name(eng) : %s, Filmography : %s ' % (
                    r['director_code'], r['code_movie'], r['title'], r['name_korean'], r['name_English'], r['work_name']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

            # 장르 검색
        elif temp == "d":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            genre = input("Enter the Genre : ")
            if returnNUM == 1:
                sql = """select distinct * from movie m, genre g where m.code_movie=g.code_movie and g.genre =  '%s'  group by m.code_movie order by m.enter_date;""" % (
                    genre)
            if returnNUM == 2:
                sql = """select distinct * from movie m, genre g where m.code_movie=g.code_movie and g.genre =  '%s' group by m.code_movie order by m.opening_date;""" % (
                    genre)
            if returnNUM == 3:
                sql = """select distinct * from movie m, genre g where m.code_movie=g.code_movie and g.genre =  '%s' group by m.code_movie  order by m.title;""" % (
                    genre)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('code_movie : %s, title : %s , genre : %s ' % (
                    r['code_movie'], r['title'], r['genre']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        # 개봉 연도를 기준으로 검색
        elif temp == "e":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            openining_date = input("Enter the opening date : ")
            if returnNUM == 1:
                sql = """select distinct * from movie m where year(m.opening_date) = '%s' group by m.code_movie order by m.enter_date;""" % (
                    openining_date)
            if returnNUM == 2:
                sql = """select distinct * from movie m where year(m.opening_date) = '%s' group by m.code_movie order by m.opening_date;""" % (
                    openining_date)
            if returnNUM == 3:
                sql = """select distinct * from movie m where year(m.opening_date) = '%s' group by m.code_movie order by m.title;""" % (
                    openining_date)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('code_movie : %s, title : %s , opening_date : %s ' % (
                    r['code_movie'], r['title'], r['opening_date']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        elif temp == "g":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            tmp = input("Enter the title : ")
            if returnNUM == 1:
                sql = """select distinct *
                                from movie m, director d
                                where m.code_movie = d.code_movie and m.title = '%s'
                                order by m.enter_date;""" % (tmp)
            if returnNUM == 2:
                sql = """select distinct *
                                from movie m, director d
                                where m.code_movie = d.code_movie and m.title = '%s' 
                                order by m.opening_date;""" % (tmp)
            if returnNUM == 3:
                sql = """select distinct *
                                from movie m, director d
                                where m.code_movie = d.code_movie and m.title = '%s'
                                order by m.title;""" % (tmp)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('code_movie : %s, title : %s ,irector_code : %s, name_korean : %s ' % (
                    r['code_movie'], r['title'], r['director_code'], r['name_korean']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        elif temp == "f":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            tmp = input("Enter the title : ")
            if returnNUM == 1:
                sql = """select distinct *
                                from movie m, actor a
                                where m.code_movie = a.code_movie and m.title = '%s'
                                order by m.enter_date;""" % (tmp)
            if returnNUM == 2:
                sql = """select distinct *
                                from movie m, actor a
                                where m.code_movie = a.code_movie and m.title = '%s'
                                order by m.opening_date;""" % (tmp)
            if returnNUM == 3:
                sql = """select distinct *
                                from movie m, actor a
                                where m.code_movie = a.code_movie and m.title = '%s'
                                order by m.title;""" % (tmp)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('code_movie : %s, itle : %s , actor_name : %s, role : %s, casting_name : %s' % (
                    r['code_movie'], r['title'], r['actor_name'], r['role'], r['casting_name']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        # 명대사 검색
        elif temp == "h":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            famous_line = input("Enter the title : ")
            if returnNUM == 1:
                sql = """select * from movie m, famous_lines f where m.code_movie = f.code_movie and m.title = '%s' order by m.enter_date;""" % (
                    famous_line)
            if returnNUM == 2:
                sql = """select * from movie m, famous_lines f where m.code_movie = f.code_movie and m.title = '%s' order by m.opening_date;""" % (
                    famous_line)
            if returnNUM == 3:
                sql = """select * from movie m, famous_lines f where m.code_movie = f.code_movie and m.title = '%s' order by m.title;""" % (
                    famous_line)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print('code_movie : %s, title : %s , famous_line : %s' % (
                    r['code_movie'], r['title'], r['famous_line']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")


        elif temp == "i":
            print("----------------------------------------------------------------\n")
            returnNUM = orderBY()
            print(returnNUM)
            print("----------------------------------------------------------------\n")
            returnNUM = int(float(returnNUM))
            sql = ""

            title = input("Enter the title : ")
            if returnNUM == 1:
                sql = """select *
                                from movie m, review r
                                where m.code_movie = r.code_movie and m.title = '%s' order by m.enter_date;""" % (title)
            if returnNUM == 2:
                sql = """select *
                                from movie m, review r
                                where m.code_movie = r.code_movie and m.title = '%s' order by m.opening_date;""" % (
                    title)
            if returnNUM == 3:
                sql = """select *
                                from movie m, review r
                                where m.code_movie = r.code_movie and m.title = '%s' order by m.title;""" % (title)

            cur.execute(sql)
            r = cur.fetchone()

            while r:
                print(
                    'code_movie : %s, title : %s , review_title : %s , review_text : %s , review_uname : %s , review_date : %s eview_good : %s' % (
                        r['code_movie'], r['title'], r['review_title'], r['review_text'], r['review_uname'],
                        r['review_date'], r['review_good']))
                r = cur.fetchone()

            print("----------------------------------------------------------------")
            print("\n")

        else:
            print("Enter again!")


if __name__ == '__main__':
    console()
