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