-- MySQL dump 10.13  Distrib 5.5.36, for Linux (i686)
--
-- Host: localhost    Database: transport_vpaslav
-- ------------------------------------------------------
-- Server version	5.5.36-cll-lve

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin'),(2,'customer'),(3,'writer');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (2,1,10),(1,1,11),(4,1,12),(9,1,19),(5,1,20),(6,1,21),(7,1,22),(8,1,23),(15,1,24),(14,1,25),(3,1,26),(13,1,27),(11,1,28),(12,1,29),(10,1,30),(17,2,10),(16,2,11),(18,2,12),(23,2,19),(19,2,20),(20,2,21),(21,2,22),(22,2,23),(27,2,24),(25,2,28),(26,2,29),(24,2,30),(29,3,10),(28,3,11),(30,3,12),(35,3,19),(31,3,20),(32,3,21),(33,3,22),(34,3,23),(39,3,24),(37,3,28),(38,3,29),(36,3,30);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add task',7,'add_task'),(20,'Can change task',7,'change_task'),(21,'Can delete task',7,'delete_task'),(22,'Can add comment',8,'add_comment'),(23,'Can change comment',8,'change_comment'),(24,'Can delete comment',8,'delete_comment'),(25,'Can add report',9,'add_report'),(26,'Can change report',9,'change_report'),(27,'Can delete report',9,'delete_report'),(28,'Can add user profile',10,'add_userprofile'),(29,'Can change user profile',10,'change_userprofile'),(30,'Can delete user profile',10,'delete_userprofile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$hqf4r49QUzju$bhfwiyL/u9UhjnIidXB97lpDcsi9rs2NDqH3/xPEdjo=','2014-03-27 15:30:40',1,'transport','','','qqqq@qqq.qq',1,1,'2014-03-27 15:28:20'),(2,'pbkdf2_sha256$12000$FCTwXQsa18o0$yMeHLlk1dJs0ZZvlkt58pY9pUHnZKjkEuBVWHVlbYhs=','2014-04-03 13:44:39',0,'admin','Admin','Admin','qqq@admin.ukr',0,1,'2014-03-27 15:32:13'),(3,'pbkdf2_sha256$12000$8xJoplG7vwxJ$eSHhnkUyH5nm9muPL3yQfDL42rsK8HNa8pAoc7MzqvI=','2014-04-03 12:51:16',0,'customer','Customer1','Customer1','foxandkamarus@gmail.com',0,1,'2014-03-27 15:33:09'),(4,'pbkdf2_sha256$12000$GIK34V3KktbZ$7NSjQoXcy4B6G0u89y072En0fdC2aWYf51DtazxfU7I=','2014-04-03 12:49:18',0,'writer','Writer','Writer','employer@tr.com',0,1,'2014-03-27 15:33:53'),(5,'pbkdf2_sha256$12000$FWrYa9ZxVEqd$z0KRdE+gYL3U6HnN6LcfAaEhm7fwnPqif4unC89JlJM=','2014-04-03 11:47:09',0,'customer1','Cust1','Cust1','wowowow@ss.ss',0,1,'2014-04-03 11:47:00'),(6,'pbkdf2_sha256$12000$7hNhFjV1vVFH$V8244nGQQdb6YsCUBwKSR5Grv6aguCEBHL1Rlh52FtA=','2014-04-03 11:49:50',0,'writer1','wririrr','wririrr','qqqqqq@qq.com',0,1,'2014-04-03 11:49:40'),(7,'pbkdf2_sha256$12000$NZWt9DmGCVme$EBuBbv/RKjm6fAkpLAK+SMPLF05mjtS0cRmUjGTntJ0=','2014-04-03 13:27:26',0,'admin1','Admin1','Admin1','wowowoww@ss.ss',0,1,'2014-04-03 13:27:16');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (4,2,1),(5,3,2),(6,4,3),(7,5,2),(8,6,3),(9,7,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime NOT NULL,
  `rating` smallint(6) NOT NULL,
  `ctask_id` int(11) NOT NULL,
  `cowner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comments_7e324c1b` (`ctask_id`),
  KEY `comments_cd0085cc` (`cowner_id`),
  CONSTRAINT `ctask_id_refs_id_7cfa6d9b` FOREIGN KEY (`ctask_id`) REFERENCES `tasks` (`id`),
  CONSTRAINT `cowner_id_refs_id_7e062414` FOREIGN KEY (`cowner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'task','general','task'),(8,'comment','comments','comment'),(9,'report','reports','report'),(10,'user profile','userprofile','userprofile');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('tud68rsk01ukwz6t6pkc88aaleg2c8ok','OGI2YTYwYmQ5YTJmMjk5MzM0MTA5ZDdhNDBiZWJlOGFjNTAyYzNkNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-04-17 13:44:40');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime NOT NULL,
  `rtask_id` int(11) NOT NULL,
  `rowner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reports_9e5f8fb0` (`rtask_id`),
  KEY `reports_d05831e3` (`rowner_id`),
  CONSTRAINT `rtask_id_refs_id_032139a7` FOREIGN KEY (`rtask_id`) REFERENCES `tasks` (`id`),
  CONSTRAINT `rowner_id_refs_id_204a6768` FOREIGN KEY (`rowner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `paper_title` varchar(100) NOT NULL,
  `discipline` varchar(100) NOT NULL,
  `assigment` varchar(100) NOT NULL,
  `level` varchar(100) NOT NULL,
  `urgency` int(11) NOT NULL,
  `spacing` smallint(6) NOT NULL,
  `page_number` smallint(6) NOT NULL,
  `style` smallint(6) NOT NULL,
  `source_number` smallint(6) NOT NULL,
  `mark` decimal(3,2) DEFAULT NULL,
  `instructions` longtext NOT NULL,
  `attach` varchar(100) DEFAULT NULL,
  `discount` varchar(100) NOT NULL,
  `accept_terms` tinyint(1) NOT NULL,
  `payment_status` smallint(6) NOT NULL,
  `priority` varchar(1) NOT NULL,
  `site` longtext,
  `ttype` smallint(6) NOT NULL,
  `access_level` varchar(1) NOT NULL,
  `revision` tinyint(1) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `assignee_id` int(11) DEFAULT NULL,
  `manager_id` int(11) DEFAULT NULL,
  `editor_id` int(11) DEFAULT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `completed` datetime DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tasks_cb902d83` (`owner_id`),
  KEY `tasks_98516953` (`assignee_id`),
  KEY `tasks_68afd4a7` (`manager_id`),
  KEY `tasks_c2be667f` (`editor_id`),
  CONSTRAINT `editor_id_refs_id_ba4d12bb` FOREIGN KEY (`editor_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `assignee_id_refs_id_ba4d12bb` FOREIGN KEY (`assignee_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `manager_id_refs_id_ba4d12bb` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `owner_id_refs_id_ba4d12bb` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'Title1','hs','es','hs',43200,1,123,1,111,NULL,'QAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZ\r\nQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQ\r\nQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQA\r\nQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQAZQA','','123',1,1,'2',NULL,1,'0',0,3,4,NULL,NULL,'2014-03-27 15:36:31','2014-04-03 12:35:39',NULL,1),(2,'Title2','ln','re','hs',21600,1,123,1,123,NULL,'wsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx','','123',1,1,'2',NULL,1,'0',0,3,NULL,NULL,NULL,'2014-03-27 15:37:05','2014-03-31 12:48:57',NULL,2),(3,'Title3','ln','re','hs',21600,1,12,1,12,NULL,'wsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx\r\nwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsxwsx','','123',1,1,'2',NULL,1,'0',0,3,NULL,NULL,NULL,'2014-03-27 15:37:39','2014-03-31 12:49:09',NULL,5),(4,'Title4','ln','re','hs',86400,1,12,2,223,NULL,'qazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqaz\r\nqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqaz\r\nqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqaz\r\nqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqazqaz\r\nqazqazqazqazqazqazqazqazqazqaz','','1234',1,1,'2',NULL,1,'0',0,3,4,NULL,NULL,'2014-03-27 15:38:14','2014-04-03 12:38:32',NULL,1),(6,'title234','ln','re','hs',21600,1,33,1,233,2.22,'title234title234title234title234title234title234title234title234title234title234title234title234title234title234\r\ntitle234title234title234title234title234title234title234title234title234title234title234title234title234title234\r\ntitle234title234title234title234title234title234title234title234title234title234title234title234title234title234\r\ntitle234title234title234title234title234title234title234title234title234title234title234title234title234title234\r\ntitle234title234title234title234title234title234title234title234title234title234title234title234title234title234','','1234',1,1,'2','85.17.249.125:8089',1,'0',1,3,4,NULL,NULL,'2014-03-31 12:51:07','2014-04-03 14:29:20',NULL,3),(8,'paepr123','lt','es','co',21600,1,123,2,123,NULL,'Schools were left shocked by poor results for exams taken in January, which will contribute towards pupils\' final marks this summer.\r\n\r\nTeachers and parents reacted angrily to what they claimed were \"unexpectedly low grades\" for exams.\r\n\r\nThe Conservatives said the report was little short of a \"whitewash\".\r\n\r\nThe report found no one single aspect contributed to the poor results.\r\n\r\nEducation Minister Huw Lewis admitted \"marking was severe\" in his response to the report to AMs on Tuesday and added that the \"results will stand but lessons will be learned\".\r\n\r\nHe called on teachers to \"exercise increased caution when predicting grades for learners\", saying that data in the report showed \"only in a minority of cases do teacher estimates match actual outcomes\".','','123',1,1,'','85.17.249.125:8089',1,'',0,3,NULL,NULL,NULL,'2014-04-02 12:45:25','2014-04-02 12:45:36',NULL,4),(9,'paer123','ln','re','hs',43200,1,123,1,123,NULL,'Schools were left shocked by poor results for exams taken in January, which will contribute towards pupils\' final marks this summer.\r\n\r\nTeachers and parents reacted angrily to what they claimed were \"unexpectedly low grades\" for exams.\r\n\r\nThe Conservatives said the report was little short of a \"whitewash\".\r\n\r\nThe report found no one single aspect contributed to the poor results.\r\n\r\nEducation Minister Huw Lewis admitted \"marking was severe\" in his response to the report to AMs on Tuesday and added that the \"results will stand but lessons will be learned\".\r\n\r\nHe called on teachers to \"exercise increased caution when predicting grades for learners\", saying that data in the report showed \"only in a minority of cases do teacher estimates match actual outcomes\".','','123',1,1,'','85.17.249.125:8089',1,'',0,3,NULL,NULL,NULL,'2014-04-02 12:49:08','2014-04-02 12:49:08',NULL,4),(10,'paper123','ln','es','hs',259200,1,123,2,123,NULL,'Schools were left shocked by poor results for exams taken in January, which will contribute towards pupils\' final marks this summer.\r\n\r\nTeachers and parents reacted angrily to what they claimed were \"unexpectedly low grades\" for exams.\r\n\r\nThe Conservatives said the report was little short of a \"whitewash\".\r\n\r\nThe report found no one single aspect contributed to the poor results.\r\n\r\nEducation Minister Huw Lewis admitted \"marking was severe\" in his response to the report to AMs on Tuesday and added that the \"results will stand but lessons will be learned\".\r\n\r\nHe called on teachers to \"exercise increased caution when predicting grades for learners\", saying that data in the report showed \"only in a minority of cases do teacher estimates match actual outcomes\".','','123',1,1,'','85.17.249.125:8089',1,'',0,3,NULL,NULL,NULL,'2014-04-02 13:26:24','2014-04-03 13:51:58',NULL,0),(11,'papeeppeppe','hs','es','co',21600,1,222,1,222,NULL,'Schools were left shocked by poor results for exams taken in January, which will contribute towards pupils\' final marks this summer.\r\n\r\nTeachers and parents reacted angrily to what they claimed were \"unexpectedly low grades\" for exams.\r\n\r\nThe Conservatives said the report was little short of a \"whitewash\".\r\n\r\nThe report found no one single aspect contributed to the poor results.\r\n\r\nEducation Minister Huw Lewis admitted \"marking was severe\" in his response to the report to AMs on Tuesday and added that the \"results will stand but lessons will be learned\".\r\n\r\nHe called on teachers to \"exercise increased caution when predicting grades for learners\", saying that data in the report showed \"only in a minority of cases do teacher estimates match actual outcomes\".','','123',1,1,'','85.17.249.125:8089',1,'',0,3,NULL,NULL,NULL,'2014-04-02 14:11:57','2014-04-02 14:12:24',NULL,0);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_profiles`
--

DROP TABLE IF EXISTS `user_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_profiles` (
  `user_ptr_id` int(11) NOT NULL,
  `gender` smallint(6) NOT NULL,
  `country` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  CONSTRAINT `user_ptr_id_refs_id_738769bc` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profiles`
--

LOCK TABLES `user_profiles` WRITE;
/*!40000 ALTER TABLE `user_profiles` DISABLE KEYS */;
INSERT INTO `user_profiles` VALUES (1,1,'ua','123','2014-03-27 16:30:36'),(2,0,'AF','123','2014-03-27 15:32:40'),(3,0,'AF','222','2014-04-02 14:20:14'),(4,0,'AF','123','2014-03-27 15:34:26'),(5,0,'BY','123','2014-04-03 11:47:00'),(6,0,'AT','1234','2014-04-03 11:50:02'),(7,0,'BY','12345','2014-04-03 13:27:21');
/*!40000 ALTER TABLE `user_profiles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-03 16:32:11
