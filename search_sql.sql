#영화 제목을 입력하고, 매칭되는 영화 정보를 검색
select distinct * from MOVIE m, TITLES_AKAS t where m.MID=t.MID and t.TITLE='%s' 

#특정 배우가 출연하는 영화를 별점이 높은 순으로 검색 
select * from MOVIE m, REVIEW r, 
	(SELECT distinct c.MID from CASTING C 
	where c.NID IN (SELECT n.NID from NAME_INFO n where n.NNAME='Ingmar Bergman') and c.category='actor') temp 
where m.MID=temp.MID and temp.MID=r.MID 
order by r.AVERAGE_RATING desc;

#특정 감독이 제작한 영화를 개봉 연도 순으로 검색 
select * 
from MOVIE m, 
	(SELECT distinct C.MID from CASTING C 
	where c.NID IN (SELECT n.NID from NAME_INFO n where n.NNAME='%') and c.category='director') temp 
where m.MID=temp.MID 
order by m.START_YEAR; 

#Drama 장르의 영화를 리뷰가 많은 순으로 검색 / Drama 장르의 영화를 별점이 높은 순으로 검색 
select * 
from MOVIE m join REVIEW r on m.MID=r.MID 
where m.MID IN (select distinct MID from GENRES where GENRE='Drama') 
order by r.NUM_VOTES desc; 
#order by r.AVERAGE_RATING desc; 

#개봉 연도를 기준으로 검색 (개봉 연도가 특정 연도 이후, 이전, 사이) 
select distinct * from MOVIE m, TITLES_AKAS t 
where m.MID=t.MID and t.TITLE='Blacksmith Scene' 
	#and m.START_YEAR <= '%s' 
order by m.START_YEAR; 

#작가가 참여한 영화 검색 
select * from MOVIE m, 
(SELECT distinct c.MID from CASTING C 
where c.NID IN (SELECT n.NID from NAME_INFO n where n.NNAME='%') and c.category='writer') temp 
where m.MID=temp.MID 
order by m.START_YEAR; 

#시즌 기준 검색 
select distinct * 
from TITLES_AKAS t, SEASON S 
where t.MID=S.PARENT_MID and t.TITLE='%s'; 

#국가 기준 검색 
select distinct * 
from MOVIE m, TITLES_AKAS t 
where m. MID=t.MID and t.REGION='%s'; 

#영화에 참여한 사람 검색 
select * from MOVIE m, 
	(SELECT distinct c.MID 
    from CASTING C 
	where c.NID IN (SELECT n.NID from NAME_INFO n where n.NNAME='%s')) temp 
where m.MID=temp.MID 
order by m.START_YEAR