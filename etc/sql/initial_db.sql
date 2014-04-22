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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
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
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add task',7,'add_task'),(20,'Can change task',7,'change_task'),(21,'Can delete task',7,'delete_task'),(22,'Can add message',8,'add_message'),(23,'Can change message',8,'change_message'),(24,'Can delete message',8,'delete_message'),(25,'Can add report',9,'add_report'),(26,'Can change report',9,'change_report'),(27,'Can delete report',9,'delete_report'),(28,'Can add user profile',10,'add_userprofile'),(29,'Can change user profile',10,'change_userprofile'),(30,'Can delete user profile',10,'delete_userprofile');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Vd9a38P5xyHa$pquwZlnbEx5/dir+UYvjiem1GzmAxBshCHCOfZstrdg=','2014-04-22 12:17:08',1,'transport','','','wwwww@www.com',1,1,'2014-04-15 12:27:25'),(2,'pbkdf2_sha256$12000$eKbqEddEt0hP$tDfzGlx02Wl9pwAKsxTRop0LsrBURBOTAl9FUIkCv6M=','2014-04-22 11:53:10',0,'admin','Admin','Admin','foxandkamarus@gmail.com',0,1,'2014-04-15 12:31:15'),(3,'pbkdf2_sha256$12000$iDEzJ6pfWoYY$TisahZaho3s6r0NjPjWfIGvdsuneQfYm3eXKaDlsz90=','2014-04-17 14:45:58',0,'customer','Customer','Customer','cust@ukt.rnt',0,1,'2014-04-15 12:31:43'),(4,'pbkdf2_sha256$12000$V4vfmI3S4fkZ$D25TeJnUBVH50YsRcMzNfRie2pUPyh1W6pvDYNk+OHw=','2014-04-15 12:32:03',0,'editor','Editor','Editor','employer@tr.com',0,1,'2014-04-15 12:32:03'),(5,'pbkdf2_sha256$12000$ZytjcJhqF2gk$fYcALTdm+3wmLhyYtJ7uJnoMzhTRRrcAAQbJH5PW1hY=','2014-04-15 12:32:28',0,'writer','Writer','Writer','employee@tr.com',0,1,'2014-04-15 12:32:29'),(6,'pbkdf2_sha256$12000$BVaZsFFBmEu4$2gJAvBhK9/81zvyfy5M9n8F6fplaRvthorKs7qlIKqU=','2014-04-15 15:11:33',0,'admin1','Admin1','Admin1','wwww@qq.qq',0,1,'2014-04-15 15:11:26');
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (6,2,1),(7,3,3),(8,4,4),(9,5,2),(10,6,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'task','general','task'),(8,'message','msgs','message'),(9,'report','reports','report'),(10,'user profile','userprofile','userprofile');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msgs`
--

DROP TABLE IF EXISTS `msgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msgs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `body` longtext NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `readby` varchar(500) NOT NULL,
  `visibility` smallint(6) NOT NULL,
  `mtask_id` int(11) NOT NULL,
  `mowner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `msgs_6861a200` (`mtask_id`),
  KEY `msgs_09424acf` (`mowner_id`),
  CONSTRAINT `mtask_id_refs_id_ca3aba33` FOREIGN KEY (`mtask_id`) REFERENCES `tasks` (`id`),
  CONSTRAINT `mowner_id_refs_id_64393281` FOREIGN KEY (`mowner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `msgs`
--

LOCK TABLES `msgs` WRITE;
/*!40000 ALTER TABLE `msgs` DISABLE KEYS */;
INSERT INTO `msgs` VALUES (1,'title111','qqqq','2014-04-17 14:46:12','2014-04-17 14:46:21',':3:',0,4,3);
/*!40000 ALTER TABLE `msgs` ENABLE KEYS */;
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
INSERT INTO `tasks` VALUES (1,'22222','ln','es','hs',21600,1,2,1,2,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','1233',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 12:45:53','2014-04-22 11:53:16',NULL,1),(2,'paper1','ln','re','hs',21600,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:08','2014-04-15 14:46:11',NULL,7),(3,'paper2','ln','ab','hs',43200,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:41','2014-04-15 14:46:44',NULL,7),(4,'Paepr2','hs','es','hs',21600,1,2,1,22,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','111',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:53:10','2014-04-15 15:10:34',NULL,1),(5,'qqqqqqqq','lt','re','co',86400,2,13,2,22,NULL,'The company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-16 13:26:29','2014-04-16 14:34:35',NULL,4);
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

-- Dump completed on 2014-04-22 14:19:50
