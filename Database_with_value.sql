/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/ lms /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE lms;

DROP TABLE IF EXISTS book;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `publishedYear` int DEFAULT NULL,
  `totalPage` int DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3459 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS booklead;
CREATE TABLE `booklead` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `book_id` int DEFAULT NULL,
  `lead_time` date DEFAULT NULL,
  `return_time` date DEFAULT NULL,
  `lead_status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS librarian;
CREATE TABLE `librarian` (
  `O_Name` varchar(100) DEFAULT NULL,
  `L_Name` varchar(100) DEFAULT NULL,
  `L_Password` varchar(100) DEFAULT NULL,
  `L_MobNo` int DEFAULT NULL,
  `L_Email` varchar(100) NOT NULL,
  PRIMARY KEY (`L_Email`),
  UNIQUE KEY `L_Email` (`L_Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS student;
CREATE TABLE `student` (
  `id` mediumint NOT NULL AUTO_INCREMENT,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `Sname` varchar(50) DEFAULT NULL,
  `RollNo` varchar(20) DEFAULT NULL,
  `RegNo` varchar(20) DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Sem` varchar(20) DEFAULT NULL,
  `Dept` varchar(50) DEFAULT NULL,
  `DOB` varchar(20) DEFAULT NULL,
  `Topic` text,
  `MobNo` int DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Locat` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `RegNo` (`RegNo`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO book(id,title,author,publishedYear,totalPage,category) VALUES(3,'cvx','gvb',1999,600,'Magazines                                         '),(4,'cvx','gvb',1999,600,'Magazines                                         '),(5,'cvx','gvb',1999,600,'Magazines                                         '),(6,'cvx','gvb',1999,600,'Magazines                                         '),(7,'cvx','gvb',1999,600,'Magazines                                         '),(8,'cvx','gvb',1999,600,'Magazines                                         '),(9,'cvx','gvb',1999,600,'Magazines                                         '),(10,'cvx','gvb',1999,600,'Magazines                                         '),(11,'cvx','gvb',1999,600,'Magazines                                         '),(12,'cvx','gvb',1999,600,'Magazines                                         '),(3456,'python programing','n. drew.',2000,235,'First Se'),(3457,'passw','sd',3424,235,'Technology');

INSERT INTO booklead(id,student_id,book_id,lead_time,return_time,lead_status) VALUES(1,5,3,'2021-11-11',NULL,0),(2,5,4,'2021-11-11','2021-11-11',1),(3,5,5,'2021-11-11','2021-11-11',1),(4,5,6,'2021-11-11','2021-11-11',1),(5,5,7,'2021-11-11',NULL,0),(6,5,4,'2021-11-11',NULL,0);

INSERT INTO librarian(O_Name,L_Name,L_Password,L_MobNo,L_Email) VALUES('x','x','s',33,'bestangle@gmail.com'),('chandan','lpu','811103',829873,'bestangleoff@gmail.com');
INSERT INTO student(id,create_time,update_time,Sname,RollNo,RegNo,Gender,Sem,Dept,DOB,Topic,MobNo,Email,Locat) VALUES(5,'2021-10-31 18:41:07','2021-10-31 18:41:10','chandan','K20@)GPA45','12112785','Male','Third','CSE','30-12-2003',X'41492026204d4c',82987378,'bestangleo',X'50616e636869'),(9,NULL,NULL,'vb','e454','454','Male','Third','ME','45',X'646464',45453,'xxdddxc',X'78787866646664'),(10,NULL,NULL,'vb','e454','4545','Male','Third','ME','45',X'646464',4556,'xxdddxcs',X'78787866646664'),(11,NULL,NULL,'vb','e454','454534','Male','Third','ME','45',X'646464',4556567,'xxdddxcsdd',X'78787866646664'),(13,NULL,NULL,'vb','e454','45453476','Male','Third','ME','45',X'646464',45587,'xxddsdfgf',X'78787866646664'),(15,NULL,NULL,'vb','e454','4545376','Male','Third','ME','45',X'646464',4558745,'xxddsdfgfsdd',X'78787866646664'),(16,NULL,NULL,'vb','e454','454576','Male','Third','ME','45',X'646464',4667,'fjfhjhg',X'78787866646664'),(17,NULL,NULL,'vb','e454','4545676','Male','Third','ME','45',X'646464',46674,'fjfhjhgs',X'78787866646664'),(18,NULL,NULL,'vb','e454','4544476','Male','Third','ME','45',X'646464',466744,'fjfhfgfjhgs',X'78787866646664'),(19,NULL,NULL,'vb','e454','45444476','Male','Third','ME','45',X'646464',46446744,'fjfhfgfdjhgs',X'78787866646664'),(20,NULL,NULL,'vb','e454','4476','Male','Third','ME','45',X'646464',4644,'fjfhfjhgs',X'78787866646664'),(21,NULL,NULL,'vb','e454','44796','Male','Third','ME','45',X'646464',46944,'fjfhfddjhgs',X'78787866646664'),(22,NULL,NULL,'vb','e454','447996','Male','Third','ME','45',X'646464',469449,'gfjghvb',X'78787866646664'),(23,NULL,NULL,'vb','e454','4479796','Male','Third','ME','45',X'646464',469477,'gfjghvbf',X'78787866646664');