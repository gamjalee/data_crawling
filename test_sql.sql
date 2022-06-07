use final;

CREATE TABLE `review_2` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `code_movie` int DEFAULT NULL,
  `review_title` varchar(45) DEFAULT NULL,
  `review_text` varchar(45) DEFAULT NULL,
  `review_uname` varchar(45) DEFAULT NULL,
  `review_date` varchar(45) DEFAULT NULL,
  `review_good` varchar(45) DEFAULT NULL,
  `enter_date` varchar(45) DEFAULT 'now()',
  PRIMARY KEY (`review_id`),
  KEY `code_movie` (`code_movie`)
  #FOREIGN KEY (`code_movie`) REFERENCES `movie` (`code_movie`)
  #movie table 없어서 주석처리
);

select * from review_2