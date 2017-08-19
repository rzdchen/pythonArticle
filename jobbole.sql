/*
SQLyog v10.2 
MySQL - 5.7.18-log : Database - jobbole
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`jobbole` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `jobbole`;

/*Table structure for table `article` */

DROP TABLE IF EXISTS `article`;

CREATE TABLE `article` (
  `tags` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `fav_nums` int(10) DEFAULT NULL,
  `front_image_url` varchar(100) DEFAULT NULL,
  `front_image_path` varchar(100) DEFAULT NULL,
  `praise_nums` int(10) DEFAULT NULL,
  `comment_nums` int(10) DEFAULT NULL,
  `content` longtext
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lagou_job` */

DROP TABLE IF EXISTS `lagou_job`;

CREATE TABLE `lagou_job` (
  `url` varchar(300) NOT NULL,
  `url_object_id` varchar(50) NOT NULL,
  `title` varchar(100) NOT NULL,
  `salary` varchar(20) DEFAULT NULL,
  `job_city` varchar(10) DEFAULT NULL,
  `work_years` varchar(100) DEFAULT NULL,
  `degree_need` varchar(30) DEFAULT NULL,
  `job_type` varchar(20) DEFAULT NULL,
  `publish_time` varchar(20) DEFAULT NULL,
  `tags` varchar(100) DEFAULT NULL,
  `job_advantage` varchar(1000) DEFAULT NULL,
  `job_desc` longtext,
  `job_addr` varchar(50) DEFAULT NULL,
  `company_url` varchar(300) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `crawl_time` datetime DEFAULT NULL,
  `crawl_update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `proxy_ip` */

DROP TABLE IF EXISTS `proxy_ip`;

CREATE TABLE `proxy_ip` (
  `proxy_ip` varchar(20) NOT NULL,
  `port` varchar(7) NOT NULL,
  `speed` float DEFAULT NULL,
  `proxy_type` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`proxy_ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `zhihu_answer` */

DROP TABLE IF EXISTS `zhihu_answer`;

CREATE TABLE `zhihu_answer` (
  `zhihu_id` bigint(20) NOT NULL,
  `url` varchar(300) DEFAULT NULL,
  `question_id` bigint(20) DEFAULT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` longtext,
  `praise_num` int(11) DEFAULT NULL,
  `comments_num` int(11) DEFAULT NULL,
  `create_time` date DEFAULT NULL,
  `update_time` date DEFAULT NULL,
  `crawl_time` datetime DEFAULT NULL,
  `crawl_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `zhihu_question` */

DROP TABLE IF EXISTS `zhihu_question`;

CREATE TABLE `zhihu_question` (
  `zhihu_id` bigint(20) NOT NULL,
  `url` varchar(300) DEFAULT NULL,
  `question_id` bigint(20) DEFAULT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` longtext,
  `praise_num` int(11) DEFAULT NULL,
  `comments_num` int(11) DEFAULT NULL,
  `create_time` date DEFAULT NULL,
  `update_time` date DEFAULT NULL,
  `crawl_time` datetime DEFAULT NULL,
  `crawl_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
