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
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (11,1,1),(13,1,2),(12,1,3),(15,1,4),(14,1,5),(17,1,6),(16,1,7),(19,1,8),(18,1,9),(21,1,10),(20,1,11),(23,1,12),(22,1,13),(25,1,14),(24,1,15),(27,1,16),(26,1,17),(33,1,18),(28,1,19),(5,1,20),(6,1,21),(7,1,22),(8,1,23),(1,1,24),(2,1,25),(3,1,26),(4,1,27),(9,1,28),(10,1,29),(31,1,30),(30,1,31),(29,1,32),(32,1,33),(44,2,1),(46,2,2),(45,2,3),(48,2,4),(47,2,5),(50,2,6),(49,2,7),(52,2,8),(51,2,9),(54,2,10),(53,2,11),(56,2,12),(55,2,13),(58,2,14),(57,2,15),(60,2,16),(59,2,17),(66,2,18),(61,2,19),(38,2,20),(39,2,21),(40,2,22),(41,2,23),(34,2,24),(35,2,25),(36,2,26),(37,2,27),(42,2,28),(43,2,29),(64,2,30),(63,2,31),(62,2,32),(65,2,33),(77,3,1),(79,3,2),(78,3,3),(81,3,4),(80,3,5),(83,3,6),(82,3,7),(85,3,8),(84,3,9),(87,3,10),(86,3,11),(89,3,12),(88,3,13),(91,3,14),(90,3,15),(93,3,16),(92,3,17),(99,3,18),(94,3,19),(71,3,20),(72,3,21),(73,3,22),(74,3,23),(67,3,24),(68,3,25),(69,3,26),(70,3,27),(75,3,28),(76,3,29),(97,3,30),(96,3,31),(95,3,32),(98,3,33),(110,4,1),(112,4,2),(111,4,3),(114,4,4),(113,4,5),(116,4,6),(115,4,7),(118,4,8),(117,4,9),(120,4,10),(119,4,11),(122,4,12),(121,4,13),(124,4,14),(123,4,15),(126,4,16),(125,4,17),(132,4,18),(127,4,19),(104,4,20),(105,4,21),(106,4,22),(107,4,23),(100,4,24),(101,4,25),(102,4,26),(103,4,27),(108,4,28),(109,4,29),(130,4,30),(129,4,31),(128,4,32),(131,4,33);
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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add comment',7,'add_comment'),(20,'Can change comment',7,'change_comment'),(21,'Can delete comment',7,'delete_comment'),(22,'Can add task',8,'add_task'),(23,'Can change task',8,'change_task'),(24,'Can delete task',8,'delete_task'),(25,'Can add user profile',9,'add_userprofile'),(26,'Can change user profile',9,'change_userprofile'),(27,'Can delete user profile',9,'delete_userprofile'),(28,'Can add upload',10,'add_upload'),(29,'Can change upload',10,'change_upload'),(30,'Can delete upload',10,'delete_upload'),(31,'Can add report',11,'add_report'),(32,'Can change report',11,'change_report'),(33,'Can delete report',11,'delete_report');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Vd9a38P5xyHa$pquwZlnbEx5/dir+UYvjiem1GzmAxBshCHCOfZstrdg=','2014-04-15 14:33:53',1,'transport','','','wwwww@www.com',1,1,'2014-04-15 12:27:25'),(2,'pbkdf2_sha256$12000$eKbqEddEt0hP$tDfzGlx02Wl9pwAKsxTRop0LsrBURBOTAl9FUIkCv6M=','2014-04-15 12:31:15',0,'admin','Admin','Admin','foxandkamarus@gmail.com',0,1,'2014-04-15 12:31:15'),(3,'pbkdf2_sha256$12000$iDEzJ6pfWoYY$TisahZaho3s6r0NjPjWfIGvdsuneQfYm3eXKaDlsz90=','2014-04-15 14:47:33',0,'customer','Customer','Customer','cust@ukt.rnt',0,1,'2014-04-15 12:31:43'),(4,'pbkdf2_sha256$12000$V4vfmI3S4fkZ$D25TeJnUBVH50YsRcMzNfRie2pUPyh1W6pvDYNk+OHw=','2014-04-15 12:32:03',0,'editor','Editor','Editor','employer@tr.com',0,1,'2014-04-15 12:32:03'),(5,'pbkdf2_sha256$12000$ZytjcJhqF2gk$fYcALTdm+3wmLhyYtJ7uJnoMzhTRRrcAAQbJH5PW1hY=','2014-04-15 12:32:28',0,'writer','Writer','Writer','employee@tr.com',0,1,'2014-04-15 12:32:29');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (5,2,1),(6,3,3),(7,4,4),(8,5,2);
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'comment','comments','comment'),(8,'report','reports','report'),(9,'task','general','task'),(10,'user profile','userprofile','userprofile'),(11,'upload','ftpstorage','upload');
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
INSERT INTO `django_session` VALUES ('5ycrr9cc2eq8dcxm8pz2v4971wn70a4f','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-04-29 14:47:33');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'22222','ln','es','hs',21600,1,2,1,2,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','1233',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 12:45:53','2014-04-15 14:46:16',NULL,7),(2,'paper1','ln','re','hs',21600,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:08','2014-04-15 14:46:11',NULL,7),(3,'paper2','ln','ab','hs',43200,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:41','2014-04-15 14:46:44',NULL,7);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploads`
--

LOCK TABLES `uploads` WRITE;
/*!40000 ALTER TABLE `uploads` DISABLE KEYS */;
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
INSERT INTO `user_profiles` VALUES (1,1,'ua','123','2014-04-15 14:30:00'),(2,0,'AF','1111','2014-04-15 12:31:36'),(3,0,'AF','1111','2014-04-15 12:32:00'),(4,0,'AF','1111','2014-04-15 12:32:25'),(5,0,'AF','1111','2014-04-15 12:32:55');
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

-- Dump completed on 2014-04-15 16:48:19
