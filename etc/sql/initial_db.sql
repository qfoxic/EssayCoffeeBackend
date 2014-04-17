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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'admin'),(3,'customer'),(4,'editor'),(2,'writer');
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
) ENGINE=InnoDB AUTO_INCREMENT=529 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (407,1,1),(409,1,2),(408,1,3),(411,1,4),(410,1,5),(413,1,6),(412,1,7),(415,1,8),(414,1,9),(417,1,10),(416,1,11),(419,1,12),(418,1,13),(421,1,14),(420,1,15),(423,1,16),(422,1,17),(429,1,18),(424,1,19),(401,1,20),(402,1,21),(403,1,22),(404,1,23),(397,1,24),(398,1,25),(399,1,26),(400,1,27),(405,1,28),(406,1,29),(427,1,30),(426,1,31),(425,1,32),(428,1,33),(440,2,1),(442,2,2),(441,2,3),(444,2,4),(443,2,5),(446,2,6),(445,2,7),(448,2,8),(447,2,9),(450,2,10),(449,2,11),(452,2,12),(451,2,13),(454,2,14),(453,2,15),(456,2,16),(455,2,17),(462,2,18),(457,2,19),(434,2,20),(435,2,21),(436,2,22),(437,2,23),(430,2,24),(431,2,25),(432,2,26),(433,2,27),(438,2,28),(439,2,29),(460,2,30),(459,2,31),(458,2,32),(461,2,33),(473,3,1),(475,3,2),(474,3,3),(477,3,4),(476,3,5),(479,3,6),(478,3,7),(481,3,8),(480,3,9),(483,3,10),(482,3,11),(485,3,12),(484,3,13),(487,3,14),(486,3,15),(489,3,16),(488,3,17),(495,3,18),(490,3,19),(467,3,20),(468,3,21),(469,3,22),(470,3,23),(463,3,24),(464,3,25),(465,3,26),(466,3,27),(471,3,28),(472,3,29),(493,3,30),(492,3,31),(491,3,32),(494,3,33),(506,4,1),(508,4,2),(507,4,3),(510,4,4),(509,4,5),(512,4,6),(511,4,7),(514,4,8),(513,4,9),(516,4,10),(515,4,11),(518,4,12),(517,4,13),(520,4,14),(519,4,15),(522,4,16),(521,4,17),(528,4,18),(523,4,19),(500,4,20),(501,4,21),(502,4,22),(503,4,23),(496,4,24),(497,4,25),(498,4,26),(499,4,27),(504,4,28),(505,4,29),(526,4,30),(525,4,31),(524,4,32),(527,4,33);
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add comment',7,'add_comment'),(20,'Can change comment',7,'change_comment'),(21,'Can delete comment',7,'delete_comment'),(22,'Can add task',8,'add_task'),(23,'Can change task',8,'change_task'),(24,'Can delete task',8,'delete_task'),(25,'Can add user profile',9,'add_userprofile'),(26,'Can change user profile',9,'change_userprofile'),(27,'Can delete user profile',9,'delete_userprofile'),(28,'Can add upload',10,'add_upload'),(29,'Can change upload',10,'change_upload'),(30,'Can delete upload',10,'delete_upload'),(31,'Can add report',11,'add_report'),(32,'Can change report',11,'change_report'),(33,'Can delete report',11,'delete_report'),(34,'Can add report',8,'add_report'),(35,'Can change report',8,'change_report'),(36,'Can delete report',8,'delete_report'),(37,'Can add task',9,'add_task'),(38,'Can change task',9,'change_task'),(39,'Can delete task',9,'delete_task'),(40,'Can add history',12,'add_history'),(41,'Can change history',12,'change_history'),(42,'Can delete history',12,'delete_history'),(43,'Can add user profile',10,'add_userprofile'),(44,'Can change user profile',10,'change_userprofile'),(45,'Can delete user profile',10,'delete_userprofile'),(46,'Can add upload',11,'add_upload'),(47,'Can change upload',11,'change_upload'),(48,'Can delete upload',11,'delete_upload');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Vd9a38P5xyHa$pquwZlnbEx5/dir+UYvjiem1GzmAxBshCHCOfZstrdg=','2014-04-15 14:33:53',1,'transport','','','wwwww@www.com',1,1,'2014-04-15 12:27:25'),(2,'pbkdf2_sha256$12000$eKbqEddEt0hP$tDfzGlx02Wl9pwAKsxTRop0LsrBURBOTAl9FUIkCv6M=','2014-04-15 12:31:15',0,'admin','Admin','Admin','foxandkamarus@gmail.com',0,1,'2014-04-15 12:31:15'),(3,'pbkdf2_sha256$12000$iDEzJ6pfWoYY$TisahZaho3s6r0NjPjWfIGvdsuneQfYm3eXKaDlsz90=','2014-04-16 14:33:18',0,'customer','Customer','Customer','cust@ukt.rnt',0,1,'2014-04-15 12:31:43'),(4,'pbkdf2_sha256$12000$V4vfmI3S4fkZ$D25TeJnUBVH50YsRcMzNfRie2pUPyh1W6pvDYNk+OHw=','2014-04-15 12:32:03',0,'editor','Editor','Editor','employer@tr.com',0,1,'2014-04-15 12:32:03'),(5,'pbkdf2_sha256$12000$ZytjcJhqF2gk$fYcALTdm+3wmLhyYtJ7uJnoMzhTRRrcAAQbJH5PW1hY=','2014-04-15 12:32:28',0,'writer','Writer','Writer','employee@tr.com',0,1,'2014-04-15 12:32:29'),(6,'pbkdf2_sha256$12000$BVaZsFFBmEu4$2gJAvBhK9/81zvyfy5M9n8F6fplaRvthorKs7qlIKqU=','2014-04-15 15:11:33',0,'admin1','Admin1','Admin1','wwww@qq.qq',0,1,'2014-04-15 15:11:26');
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (30,2,1),(31,3,3),(32,4,4),(33,5,2),(9,6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(8,'report','reports','report'),(9,'task','general','task'),(10,'user profile','userprofile','userprofile'),(11,'upload','ftpstorage','upload'),(12,'history','history','history');
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
INSERT INTO `django_session` VALUES ('hdlj6h9jlsaiuf0wa4cyflm51ib0pbfk','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-04-30 14:33:18');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `howner_id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  `object_type` varchar(12) NOT NULL,
  `action_type` varchar(6) NOT NULL,
  `created` datetime NOT NULL,
  `fields` varchar(500) NOT NULL,
  `old_values` varchar(300) NOT NULL,
  `new_values` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `history_3d8adc88` (`howner_id`),
  CONSTRAINT `howner_id_refs_id_537ac3ef` FOREIGN KEY (`howner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (2,3,5,'task','change','2014-04-16 14:33:25','spacing','spacing=2','spacing=1'),(3,3,5,'task','change','2014-04-16 14:33:33','assigment','assigment=es','assigment=re'),(4,3,5,'task','change','2014-04-16 14:34:35','discipline,spacing,style,urgency','discipline=hs,spacing=1,style=1,urgency=21600','discipline=lt,spacing=2,style=2,urgency=86400');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
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
  `discount` varchar(100) NOT NULL,
  `accept_terms` tinyint(1) NOT NULL,
  `payment_status` smallint(6) NOT NULL,
  `priority` tinyint(1) NOT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'22222','ln','es','hs',21600,1,2,1,2,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','1233',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 12:45:53','2014-04-15 14:46:16',NULL,7),(2,'paper1','ln','re','hs',21600,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:08','2014-04-15 14:46:11',NULL,7),(3,'paper2','ln','ab','hs',43200,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:41','2014-04-15 14:46:44',NULL,7),(4,'Paepr2','hs','es','hs',21600,1,2,1,22,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','111',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:53:10','2014-04-15 15:10:34',NULL,1),(5,'qqqqqqqq','lt','re','co',86400,2,13,2,22,NULL,'The company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-16 13:26:29','2014-04-16 14:34:35',NULL,4);
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uploads`
--

DROP TABLE IF EXISTS `uploads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `uploads` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `attach` varchar(100) DEFAULT NULL,
  `fowner_id` int(11) NOT NULL,
  `ftask_id` int(11) NOT NULL,
  `access_level` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uploads_0455f6ba` (`fowner_id`),
  KEY `uploads_1c473884` (`ftask_id`),
  CONSTRAINT `fowner_id_refs_id_5d3b60be` FOREIGN KEY (`fowner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ftask_id_refs_id_51147dce` FOREIGN KEY (`ftask_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploads`
--

LOCK TABLES `uploads` WRITE;
/*!40000 ALTER TABLE `uploads` DISABLE KEYS */;
INSERT INTO `uploads` VALUES (6,'2014-04-15 15:15:00','2014-04-15 15:15:00','admin1/denise_milani.jpg',6,4,'0');
/*!40000 ALTER TABLE `uploads` ENABLE KEYS */;
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
INSERT INTO `user_profiles` VALUES (1,1,'ua','123','2014-04-15 14:30:00'),(2,0,'AF','1111','2014-04-15 12:31:36'),(3,0,'AF','1111','2014-04-15 12:32:00'),(4,0,'AF','1111','2014-04-15 12:32:25'),(5,0,'AF','1111','2014-04-15 12:32:55'),(6,0,'AF','123','2014-04-15 15:11:26');
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

-- Dump completed on 2014-04-17 12:32:40
