-- MySQL dump 10.13  Distrib 5.5.37, for Linux (i686)
--
-- Host: localhost    Database: transport
-- ------------------------------------------------------
-- Server version	5.5.37-log

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
  `name` varchar(80) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
  `name` varchar(50) COLLATE utf16_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add task',7,'add_task'),(20,'Can change task',7,'change_task'),(21,'Can delete task',7,'delete_task'),(22,'Can add history',8,'add_history'),(23,'Can change history',8,'change_history'),(24,'Can delete history',8,'delete_history'),(25,'Can add message',9,'add_message'),(26,'Can change message',9,'change_message'),(27,'Can delete message',9,'delete_message'),(28,'Can add report',10,'add_report'),(29,'Can change report',10,'change_report'),(30,'Can delete report',10,'delete_report'),(31,'Can add upload',11,'add_upload'),(32,'Can change upload',11,'change_upload'),(33,'Can delete upload',11,'delete_upload'),(34,'Can add user profile',12,'add_userprofile'),(35,'Can change user profile',12,'change_userprofile'),(36,'Can delete user profile',12,'delete_userprofile'),(37,'Can add payment',13,'add_payment'),(38,'Can change payment',13,'change_payment'),(39,'Can delete payment',13,'delete_payment');
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
  `password` varchar(128) COLLATE utf16_unicode_ci NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `last_name` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `email` varchar(75) COLLATE utf16_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Vd9a38P5xyHa$pquwZlnbEx5/dir+UYvjiem1GzmAxBshCHCOfZstrdg=','2014-04-22 12:17:08',1,'transport','','','wwwww@www.com',1,1,'2014-04-15 12:27:25'),(2,'pbkdf2_sha256$12000$eKbqEddEt0hP$tDfzGlx02Wl9pwAKsxTRop0LsrBURBOTAl9FUIkCv6M=','2014-06-04 04:08:13',0,'admin','Admin','Admin','foxandkamarus@gmail.com',0,1,'2014-04-15 12:31:15'),(3,'pbkdf2_sha256$12000$iDEzJ6pfWoYY$TisahZaho3s6r0NjPjWfIGvdsuneQfYm3eXKaDlsz90=','2014-04-17 14:45:58',0,'customer','Customer','Customer','cust@ukt.rnt',0,1,'2014-04-15 12:31:43'),(4,'pbkdf2_sha256$12000$V4vfmI3S4fkZ$D25TeJnUBVH50YsRcMzNfRie2pUPyh1W6pvDYNk+OHw=','2014-04-15 12:32:03',0,'editor','Editor','Editor','employer@tr.com',0,1,'2014-04-15 12:32:03'),(5,'pbkdf2_sha256$12000$ZytjcJhqF2gk$fYcALTdm+3wmLhyYtJ7uJnoMzhTRRrcAAQbJH5PW1hY=','2014-04-15 12:32:28',0,'writer','Writer','Writer','employee@tr.com',0,1,'2014-04-15 12:32:29'),(6,'pbkdf2_sha256$12000$BVaZsFFBmEu4$2gJAvBhK9/81zvyfy5M9n8F6fplaRvthorKs7qlIKqU=','2014-04-15 15:11:33',0,'admin1','Admin1','Admin1','wwww@qq.qq',0,1,'2014-04-15 15:11:26'),(7,'pbkdf2_sha256$12000$UCjfkJ9H5Agm$plRMF4kSyIkTr2qvrZ2Z++SSEW5SWAI/0mqHblmb1lo=','2014-06-05 11:57:47',0,'Customer10','Customer','Customer','cust@gmail.com',0,1,'2014-06-05 11:57:37'),(8,'pbkdf2_sha256$12000$edjCv6HVnomy$BsxsSjIc+ElQQ+8DfPH2LFLXxWUr4kil70AwFokQeLs=','2014-06-19 19:16:27',0,'Newcustomer','Newcustomer','Newcustomer','Newcustomer@gmailc.om',0,1,'2014-06-19 19:16:27'),(9,'pbkdf2_sha256$12000$qblocARgP7un$SHgRZirwu2KcfjPohEVcZlGxM3KwGOh5u0vdJL6rh1E=','2014-06-19 19:16:44',0,'Newcustomer123','Newcustomer','Newcustomer','Newcustomer@gmailc.om',0,1,'2014-06-19 19:16:37'),(10,'pbkdf2_sha256$12000$xIWXwz0DiW8s$DkngV270v/rTEU7qe+sk89t89J0Ny4teJECnAZBzImc=','2014-06-20 12:47:31',0,'newscustomer12345','','','',0,1,'2014-06-20 12:47:22');
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
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (62,2,1),(63,3,3),(64,4,4),(65,5,2),(66,6,1),(67,7,3),(68,8,3),(69,9,3),(70,10,3);
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
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
  `object_id` longtext COLLATE utf16_unicode_ci,
  `object_repr` varchar(200) COLLATE utf16_unicode_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
  `name` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `app_label` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'task','general','task'),(8,'history','history','history'),(9,'message','msgs','message'),(10,'report','reports','report'),(11,'upload','ftpstorage','upload'),(12,'user profile','userprofile','userprofile'),(13,'payment','payments','payment');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf16_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf16_unicode_ci NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0f2tc4p0rco4bcrllngvkfwsv0gu5ags','ZjdhMGM4NjVhZmIxYmM0ODk3NzNiMzI1OGFjNWZiMWExNjljYzM3Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-06-20 14:31:22'),('8nmsp5jdm8pplbd2144hjjmg1tevxvba','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-06-27 14:43:25'),('8sn61i27p6ror15lw01sp52a2g43eus0','ZjdhMGM4NjVhZmIxYmM0ODk3NzNiMzI1OGFjNWZiMWExNjljYzM3Yzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-06-18 04:08:13'),('9f6y8wr3imztq2c3e5ogoznfp1kg1xhz','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-06-18 04:26:28'),('ai97o7g40aij7h5h88fa2w00nqigadci','OWVlZDA2ZjQ1NGNlMWQ2NGY5ODM2MGNlNjQyNDFjNDA2NmU3ZThjNTp7fQ==','2014-06-18 03:38:06'),('bpjpiu6oq1dxn965tcyfejpkj3fyj01w','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-06-22 19:26:07'),('brjxmcf78tbunb7dx7w7z1en5igy0am5','MWI3NzdiZTc3Yjk4NjMxN2RmYjU1ODAyYTkyMTQyZWQ0MWQ1NDc5OTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6OX0=','2014-07-03 19:16:44'),('dvkqp4u5fzto25c3nkdv9wrkm0ibc9pj','YjA0MWZjNzgwZjI2MTE4MTkxNTVmNmM0MmEzMDg0NDRhZGU3NGQ3NDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6N30=','2014-06-19 11:57:48'),('jbyem3epfb4ghxyy0tqvchmia7ralt7r','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-07-02 05:04:33'),('lcy2ev6pq3gbtilel7dpi26g2w8q97ob','OWVlZDA2ZjQ1NGNlMWQ2NGY5ODM2MGNlNjQyNDFjNDA2NmU3ZThjNTp7fQ==','2014-06-18 03:38:06'),('mm0jkyh8ekjl2vjrfn6d8tkchawiwxen','ZDUyZTNlYmMxMzUyNDgxYWFiYzg2YWFmNTUzMzYzMzgzYmUyOTNhNjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6M30=','2014-06-23 09:38:23'),('rhox8ao63pxzvz23cvk0fxol7zku7mlz','ZGM1ZTVhNDg0YTQwOGQ3ZmM0MjgyMzVmMmJlYTdlZWE0ZGRkOWE4ZDp7fQ==','2014-06-22 19:27:32'),('rkk7azau6e52wim5omjevyg9tn3tdo61','NDMwZTBkODVjNTJiNzYyOTFhYjNiYTM4NWYxNWZhZTMwMzM0YjkzNjp7fQ==','2014-06-18 03:38:06'),('rkzr6sfm0uh93a3ve2es9sfhc9lx7x78','ZjU0YjgwZDdkOGI1ZmJmYzM5NGEwMTEzOTg3ZmQ1ZDYyMTk2NzI2ODp7fQ==','2014-06-18 03:38:06'),('udv387z5l40tif311gk5ut8qxl5xw2oe','OTEzZGRjZTM5NmRjMzZhZGVlZDdiNDc5ZjNhZGYzZjcyYmFjYzlkODp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MTB9','2014-07-04 12:47:31'),('xfvp55lwezqjceiqeyu92rkdcvqyxag2','ZDUyZGU4YzlmODZlMGI1YWIwODUzNzM2MDViMGM5NTgxNmZlNTZiYTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6InVzZXJwcm9maWxlLmF1dGguVXNlclByb2ZpbGVCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6NX0=','2014-06-20 14:30:42');
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
  `howner_id` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `object_id` int(11) NOT NULL,
  `object_type` varchar(12) COLLATE utf16_unicode_ci NOT NULL,
  `action_type` varchar(6) COLLATE utf16_unicode_ci NOT NULL,
  `fields` varchar(1000) COLLATE utf16_unicode_ci NOT NULL,
  `created` datetime NOT NULL,
  `old_values` varchar(1500) COLLATE utf16_unicode_ci NOT NULL,
  `new_values` varchar(1500) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `history_3d8adc88` (`howner_id`),
  CONSTRAINT `howner_id_refs_id_537ac3ef` FOREIGN KEY (`howner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (1,2,2,2,'UserProfile','change','assignee,country,editor,manager','2014-06-04 04:08:41','assignee=<django.db.models.fields.related.RelatedManager object at 0xa7ad1ec>,country=AF,editor=<django.db.models.fields.related.RelatedManager object at 0xa7ad1ec>,manager=<django.db.models.fields.related.RelatedManager object at 0xa7ad94c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xa7ad9cc>,country=AZ,editor=<django.db.models.fields.related.RelatedManager object at 0xa7ad94c>,manager=<django.db.models.fields.related.RelatedManager object at 0xa7adacc>'),(2,2,2,2,'UserProfile','change','assignee,country,editor,manager','2014-06-04 04:09:57','assignee=<django.db.models.fields.related.RelatedManager object at 0xb599dd8c>,country=AZ,editor=<django.db.models.fields.related.RelatedManager object at 0xb599dd8c>,manager=<django.db.models.fields.related.RelatedManager object at 0xb598230c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xb599d74c>,country=BY,editor=<django.db.models.fields.related.RelatedManager object at 0xb599d74c>,manager=<django.db.models.fields.related.RelatedManager object at 0xb599d74c>'),(3,2,2,2,'UserProfile','change','assignee,country,editor,manager','2014-06-04 04:10:57','assignee=<django.db.models.fields.related.RelatedManager object at 0xb5bb5d2c>,country=BY,editor=<django.db.models.fields.related.RelatedManager object at 0xb5bb5d2c>,manager=<django.db.models.fields.related.RelatedManager object at 0xb5bb5e2c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xb5bb5fec>,country=AT,editor=<django.db.models.fields.related.RelatedManager object at 0xb5bb5e2c>,manager=<django.db.models.fields.related.RelatedManager object at 0xb5bb5b6c>'),(4,3,NULL,6,'Task','new','','2014-06-05 05:43:04','',''),(5,3,6,6,'Task','change','assigment,urgency','2014-06-05 05:50:58','assigment=re,urgency=2073600','assigment=ab,urgency=21600'),(6,3,6,6,'Task','change','','2014-06-05 06:09:03','',''),(7,3,6,6,'Task','change','spacing','2014-06-05 06:09:16','spacing=1','spacing=2'),(8,3,6,6,'Task','change','spacing','2014-06-05 06:09:25','spacing=2','spacing=1'),(9,NULL,NULL,7,'UserProfile','new','assignee,editor,manager','2014-06-05 11:57:37','assignee=<django.db.models.fields.related.RelatedManager object at 0xac64b56c>,editor=<django.db.models.fields.related.RelatedManager object at 0xac64b56c>,manager=<django.db.models.fields.related.RelatedManager object at 0xac64b56c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xabe090ec>,editor=<django.db.models.fields.related.RelatedManager object at 0xabe090ec>,manager=<django.db.models.fields.related.RelatedManager object at 0xac64b40c>'),(10,NULL,NULL,7,'UserProfile','change','assignee,date_joined,editor,last_login,manager,updated','2014-06-05 11:57:37','assignee=<django.db.models.fields.related.RelatedManager object at 0xac62b14c>,date_joined=2014-06-05 11:57:37+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xac62b1cc>,last_login=2014-06-05 11:57:37+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xac62b56c>,updated=2014-06-05 11:57:37+00:00','assignee=<django.db.models.fields.related.RelatedManager object at 0xac62b56c>,date_joined=2014-06-05 11:57:37.364090+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xac62b14c>,last_login=2014-06-05 11:57:37.364090+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xac62b14c>,updated=2014-06-05 11:57:37.536687+00:00'),(11,NULL,NULL,7,'UserProfile','change','assignee,editor,last_login,manager','2014-06-05 11:57:47','assignee=<django.db.models.fields.related.RelatedManager object at 0xac6c7aec>,editor=<django.db.models.fields.related.RelatedManager object at 0xac6c770c>,last_login=2014-06-05 11:57:37+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xac6c7a6c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xac6c7a6c>,editor=<django.db.models.fields.related.RelatedManager object at 0xac6c7aec>,last_login=2014-06-05 11:57:47.403363+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xac6c7aec>'),(12,7,NULL,7,'Task','new','','2014-06-05 11:58:31','',''),(13,7,NULL,8,'Task','new','','2014-06-05 11:59:25','',''),(14,7,NULL,9,'Task','new','','2014-06-05 11:59:50','',''),(15,7,9,9,'Task','change','status','2014-06-05 12:00:53','status=4','status=7'),(16,7,NULL,10,'Task','new','','2014-06-05 12:05:02','',''),(17,7,NULL,11,'Task','new','','2014-06-05 12:06:45','',''),(18,7,NULL,12,'Task','new','','2014-06-05 12:17:48','',''),(19,7,NULL,13,'Task','new','','2014-06-05 12:19:34','',''),(20,7,7,7,'Task','change','level,page_number,urgency','2014-06-05 12:20:30','level=co,page_number=2,urgency=43200','level=hs,page_number=1,urgency=21600'),(21,7,7,7,'Task','change','spacing','2014-06-05 12:20:42','spacing=1','spacing=2'),(22,7,7,7,'Task','change','urgency','2014-06-05 12:20:52','urgency=21600','urgency=1036800'),(23,7,7,7,'Task','change','urgency','2014-06-05 12:21:05','urgency=1036800','urgency=2073600'),(24,7,7,7,'Task','change','level','2014-06-05 12:21:25','level=hs','level=ph'),(25,7,7,7,'Task','change','status','2014-06-06 14:31:03','status=4','status=7'),(26,2,2,2,'Task','change','access_level,status','2014-06-06 14:31:30','access_level=1,status=7','access_level=0,status=1'),(27,3,NULL,14,'Task','new','','2014-06-09 09:41:37','',''),(28,3,14,14,'Task','change','style','2014-06-09 09:41:49','style=1','style=2'),(29,3,1,1,'Message','change','','2014-06-09 09:42:25','',''),(30,3,6,7,'Upload','new','','2014-06-09 09:44:09','',''),(31,3,7,7,'Upload','change','attach','2014-06-09 09:44:57','attach=customer/001_overview.pdf','attach='),(32,3,7,7,'Upload','delete','','2014-06-09 09:44:57','',''),(33,3,3,3,'UserProfile','change','assignee,editor,last_login,manager','2014-06-13 14:43:25','assignee=<django.db.models.fields.related.RelatedManager object at 0xa998764c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa998764c>,last_login=2014-06-09 09:37:00+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa998768c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9987a8c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa998768c>,last_login=2014-06-13 14:43:25.449557+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa998728c>'),(34,3,NULL,15,'Task','new','','2014-06-13 14:44:04','',''),(35,3,NULL,16,'Task','new','','2014-06-13 14:44:31','',''),(36,3,NULL,17,'Task','new','','2014-06-15 08:42:58','',''),(37,3,NULL,25,'Task','new','ptask','2014-06-17 06:27:26','ptask=<django.db.models.fields.related.RelatedManager object at 0xb59c1f4c>','ptask=<django.db.models.fields.related.RelatedManager object at 0xb59c1f8c>'),(38,3,NULL,26,'Task','new','ptask','2014-06-17 06:28:18','ptask=<django.db.models.fields.related.RelatedManager object at 0xb59c1fac>','ptask=<django.db.models.fields.related.RelatedManager object at 0xb59c1e8c>'),(39,3,26,26,'Task','change','ptask,status','2014-06-17 07:01:24','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2b9cc>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2b9ec>,status=7'),(40,3,26,26,'Task','change','ptask,status','2014-06-17 07:02:54','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673c3ec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673c8cc>,status=7'),(41,3,26,26,'Task','change','ptask,status','2014-06-17 07:04:09','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a6308c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a3dfac>,status=7'),(42,3,26,26,'Task','change','ptask,status','2014-06-17 07:07:03','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676d90c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a19eac>,status=7'),(43,3,26,26,'Task','change','ptask,status','2014-06-18 04:14:54','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a292ec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2998c>,status=7'),(44,3,26,26,'Task','change','ptask,status','2014-06-18 05:54:36','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5924e4c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5924fac>,status=7'),(45,3,26,26,'Task','change','ptask,status','2014-06-18 05:55:22','ptask=<django.db.models.fields.related.RelatedManager object at 0xb6729f4c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xa04d1ec>,status=7'),(46,3,26,26,'Task','change','ptask,status','2014-06-18 05:57:27','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673f76c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673ff0c>,status=7'),(47,3,26,26,'Task','change','ptask,status','2014-06-18 05:58:54','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676e2ec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673c98c>,status=7'),(48,3,26,26,'Task','change','ptask,status','2014-06-18 06:00:32','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5924e4c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5924fac>,status=7'),(49,3,26,26,'Task','change','ptask,status','2014-06-18 06:26:02','ptask=<django.db.models.fields.related.RelatedManager object at 0xb6729e2c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb6729dac>,status=7'),(50,3,25,25,'Task','change','ptask,status','2014-06-18 06:26:44','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673c32c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673e6cc>,status=7'),(51,3,26,26,'Task','change','ptask,status','2014-06-18 06:27:46','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676ddac>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676d78c>,status=7'),(52,3,26,26,'Task','change','ptask,status','2014-06-18 06:30:23','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673aaec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673af2c>,status=7'),(53,3,26,26,'Task','change','ptask,status','2014-06-18 06:31:46','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2c30c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2c96c>,status=7'),(54,3,26,26,'Task','change','ptask,status','2014-06-18 06:33:53','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676e38c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb676e26c>,status=7'),(55,3,26,26,'Task','change','ptask,status','2014-06-18 06:40:15','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2a2ec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2a94c>,status=7'),(56,3,26,26,'Task','change','ptask,status','2014-06-18 06:41:07','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673f46c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb673f7cc>,status=7'),(57,3,26,26,'Task','change','ptask,status','2014-06-18 06:43:07','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a175ac>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a1752c>,status=7'),(58,3,26,26,'Task','change','ptask,status','2014-06-18 06:46:29','ptask=<django.db.models.fields.related.RelatedManager object at 0xb6729cac>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb6729e2c>,status=7'),(59,NULL,NULL,8,'UserProfile','new','assignee,editor,manager,powner','2014-06-19 19:16:30','assignee=<django.db.models.fields.related.RelatedManager object at 0xa971cb2c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa971cb2c>,manager=<django.db.models.fields.related.RelatedManager object at 0xa9766b0c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9766b0c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xa971c94c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa971c94c>,manager=<django.db.models.fields.related.RelatedManager object at 0xa971c94c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa971c94c>'),(60,NULL,NULL,8,'UserProfile','change','assignee,date_joined,editor,last_login,manager,powner,updated','2014-06-19 19:16:30','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9766dac>,date_joined=2014-06-19 19:16:27+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xa976694c>,last_login=2014-06-19 19:16:27+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa976696c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa97668ac>,updated=2014-06-19 19:16:27+00:00','assignee=<django.db.models.fields.related.RelatedManager object at 0xa976696c>,date_joined=2014-06-19 19:16:27.155761+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xa9766dac>,last_login=2014-06-19 19:16:27.155761+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa9766dac>,powner=<django.db.models.fields.related.RelatedManager object at 0xa976696c>,updated=2014-06-19 19:16:27.286450+00:00'),(61,NULL,NULL,9,'UserProfile','new','assignee,editor,manager,powner','2014-06-19 19:16:37','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9a8924c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa9a8980c>,manager=<django.db.models.fields.related.RelatedManager object at 0xa9a89d6c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9a89d0c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9a89d6c>,editor=<django.db.models.fields.related.RelatedManager object at 0xa9a8924c>,manager=<django.db.models.fields.related.RelatedManager object at 0xa9a8924c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9a89d6c>'),(62,NULL,NULL,9,'UserProfile','change','assignee,date_joined,editor,last_login,manager,powner,updated','2014-06-19 19:16:37','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9a89d0c>,date_joined=2014-06-19 19:16:37+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xa9a89c0c>,last_login=2014-06-19 19:16:37+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa9a8704c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9a87fec>,updated=2014-06-19 19:16:37+00:00','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9a89c0c>,date_joined=2014-06-19 19:16:37.214580+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xa9a89d0c>,last_login=2014-06-19 19:16:37.214580+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa9a89d0c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9a89d0c>,updated=2014-06-19 19:16:37.348783+00:00'),(63,NULL,NULL,9,'UserProfile','change','assignee,editor,last_login,manager,powner','2014-06-19 19:16:44','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9766acc>,editor=<django.db.models.fields.related.RelatedManager object at 0xa9766dec>,last_login=2014-06-19 19:16:37+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa9a9d60c>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9a9dd6c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xa9766dec>,editor=<django.db.models.fields.related.RelatedManager object at 0xa9766acc>,last_login=2014-06-19 19:16:44.301101+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xa9766acc>,powner=<django.db.models.fields.related.RelatedManager object at 0xa9766acc>'),(64,3,17,17,'Task','change','ptask,status','2014-06-20 05:05:34','ptask=<django.db.models.fields.related.RelatedManager object at 0xb696906c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb696928c>,status=7'),(65,3,16,16,'Task','change','ptask,status','2014-06-20 05:56:55','ptask=<django.db.models.fields.related.RelatedManager object at 0xb683bd8c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb683d94c>,status=7'),(66,NULL,NULL,10,'UserProfile','new','assignee,editor,manager,powner','2014-06-20 12:47:22','assignee=<django.db.models.fields.related.RelatedManager object at 0xabdad90c>,editor=<django.db.models.fields.related.RelatedManager object at 0xabdad90c>,manager=<django.db.models.fields.related.RelatedManager object at 0xabdade0c>,powner=<django.db.models.fields.related.RelatedManager object at 0xabdade0c>','assignee=<django.db.models.fields.related.RelatedManager object at 0xabdad6cc>,editor=<django.db.models.fields.related.RelatedManager object at 0xabdade0c>,manager=<django.db.models.fields.related.RelatedManager object at 0xabdade6c>,powner=<django.db.models.fields.related.RelatedManager object at 0xabdad4ac>'),(67,NULL,NULL,10,'UserProfile','change','assignee,date_joined,editor,last_login,manager,powner,updated','2014-06-20 12:47:22','assignee=<django.db.models.fields.related.RelatedManager object at 0xabdadcec>,date_joined=2014-06-20 12:47:22+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xabdade6c>,last_login=2014-06-20 12:47:22+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xabdadc2c>,powner=<django.db.models.fields.related.RelatedManager object at 0xabdad08c>,updated=2014-06-20 12:47:22+00:00','assignee=<django.db.models.fields.related.RelatedManager object at 0xabdadc2c>,date_joined=2014-06-20 12:47:22.601248+00:00,editor=<django.db.models.fields.related.RelatedManager object at 0xabdadcec>,last_login=2014-06-20 12:47:22.601248+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xabdadcec>,powner=<django.db.models.fields.related.RelatedManager object at 0xabdadc2c>,updated=2014-06-20 12:47:22.712919+00:00'),(68,NULL,NULL,10,'UserProfile','change','assignee,editor,last_login,manager,powner','2014-06-20 12:47:31','assignee=<django.db.models.fields.related.RelatedManager object at 0xabd542ec>,editor=<django.db.models.fields.related.RelatedManager object at 0xabd54e4c>,last_login=2014-06-20 12:47:22+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xabd544ec>,powner=<django.db.models.fields.related.RelatedManager object at 0xabd54ecc>','assignee=<django.db.models.fields.related.RelatedManager object at 0xabd544ec>,editor=<django.db.models.fields.related.RelatedManager object at 0xabd542ec>,last_login=2014-06-20 12:47:31.498613+00:00,manager=<django.db.models.fields.related.RelatedManager object at 0xabd542ec>,powner=<django.db.models.fields.related.RelatedManager object at 0xabd544ec>'),(69,10,NULL,27,'Task','new','ptask','2014-06-20 12:49:55','ptask=<django.db.models.fields.related.RelatedManager object at 0xabd6da6c>','ptask=<django.db.models.fields.related.RelatedManager object at 0xabd6d0ec>'),(70,10,27,27,'Task','change','ptask','2014-06-20 12:54:37','ptask=<django.db.models.fields.related.RelatedManager object at 0xabdca50c>','ptask=<django.db.models.fields.related.RelatedManager object at 0xabdca0ec>'),(71,3,15,15,'Task','change','ptask,status','2014-06-21 20:32:50','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5b2a04c>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb5a2df4c>,status=7'),(72,3,6,6,'Task','change','ptask,status','2014-06-21 21:15:37','ptask=<django.db.models.fields.related.RelatedManager object at 0xb4f9c4ec>,status=4','ptask=<django.db.models.fields.related.RelatedManager object at 0xb4f9c6cc>,status=7');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `msgs`
--

DROP TABLE IF EXISTS `msgs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `msgs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `body` longtext COLLATE utf16_unicode_ci NOT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `readby` varchar(500) COLLATE utf16_unicode_ci NOT NULL,
  `visibility` smallint(6) NOT NULL,
  `mtask_id` int(11) NOT NULL,
  `mowner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `msgs_6861a200` (`mtask_id`),
  KEY `msgs_09424acf` (`mowner_id`),
  CONSTRAINT `mowner_id_refs_id_64393281` FOREIGN KEY (`mowner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `mtask_id_refs_id_ca3aba33` FOREIGN KEY (`mtask_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `powner_id` int(11) DEFAULT NULL,
  `ptask_id` int(11) DEFAULT NULL,
  `payment_status` smallint(6) NOT NULL,
  `payment_type` smallint(6) DEFAULT NULL,
  `created` datetime NOT NULL,
  `updated` datetime NOT NULL,
  `values` varchar(5000) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `payments_37f75f85` (`powner_id`),
  KEY `payments_a5cb3cbb` (`ptask_id`),
  CONSTRAINT `powner_id_refs_id_650e1b5b` FOREIGN KEY (`powner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ptask_id_refs_id_089b5af7` FOREIGN KEY (`ptask_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
INSERT INTO `payments` VALUES (2,3,15,2,1,'2014-06-21 20:32:50','2014-06-21 20:32:50','{}'),(3,3,15,3,1,'2014-06-21 21:08:44','2014-06-21 21:08:44','{\"payment_id\": 40980969, \"status\": \"sandbox\", \"description\": \"11111111111111111111111111111111\", \"order_id\": \"15\", \"currency\": \"UAH\", \"amount\": 0.10000000000000001, \"result\": \"ok\"}'),(4,3,6,2,1,'2014-06-21 21:15:37','2014-06-21 21:15:37','{}'),(5,3,6,3,1,'2014-06-21 21:17:09','2014-06-21 21:17:09','{\"payment_id\": 40981660, \"status\": \"sandbox\", \"description\": \"first calculation of price\", \"order_id\": \"6\", \"currency\": \"UAH\", \"amount\": 0.10000000000000001, \"result\": \"ok\"}');
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `body` longtext COLLATE utf16_unicode_ci NOT NULL,
  `created` datetime NOT NULL,
  `rtask_id` int(11) NOT NULL,
  `rowner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reports_9e5f8fb0` (`rtask_id`),
  KEY `reports_d05831e3` (`rowner_id`),
  CONSTRAINT `rowner_id_refs_id_204a6768` FOREIGN KEY (`rowner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `rtask_id_refs_id_032139a7` FOREIGN KEY (`rtask_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
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
  `paper_title` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `discipline` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `assigment` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `level` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `urgency` int(11) NOT NULL,
  `spacing` smallint(6) NOT NULL,
  `page_number` smallint(6) NOT NULL,
  `style` smallint(6) NOT NULL,
  `source_number` smallint(6) NOT NULL,
  `mark` decimal(3,2) DEFAULT NULL,
  `instructions` longtext COLLATE utf16_unicode_ci NOT NULL,
  `discount` varchar(100) COLLATE utf16_unicode_ci DEFAULT NULL,
  `accept_terms` tinyint(1) NOT NULL,
  `priority` tinyint(1) NOT NULL,
  `site` longtext COLLATE utf16_unicode_ci,
  `ttype` smallint(6) NOT NULL,
  `access_level` varchar(1) COLLATE utf16_unicode_ci NOT NULL,
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
  CONSTRAINT `assignee_id_refs_id_ba4d12bb` FOREIGN KEY (`assignee_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `editor_id_refs_id_ba4d12bb` FOREIGN KEY (`editor_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `manager_id_refs_id_ba4d12bb` FOREIGN KEY (`manager_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `owner_id_refs_id_ba4d12bb` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,'22222','ln','es','hs',21600,1,2,1,2,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','1233',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 12:45:53','2014-04-22 11:53:16',NULL,1),(2,'paper1','ln','re','hs',21600,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:08','2014-04-15 14:46:11',NULL,7),(3,'paper2','ln','ab','hs',43200,1,1,1,1,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:46:41','2014-04-15 14:46:44',NULL,7),(4,'Paepr2','hs','es','hs',21600,1,2,1,22,NULL,'Michael Jackson\'s mother has been ordered by a US court to pay AEG Live $800,000 (£480,000) for costs defending the failed negligence case she brought against the concert promoter.\r\n\r\nThe company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','111',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-15 14:53:10','2014-04-15 15:10:34',NULL,1),(5,'qqqqqqqq','lt','re','co',86400,2,13,2,22,NULL,'The company was cleared of liability over the 2009 death of the pop star in a five-month trial last October.\r\n\r\nAEG Live had sought $1.2m (£720,000) to cover costs, but Katherine Jackson\'s lawyers claimed it was not justified.\r\n\r\nBoth parties agreed not to challenge the court\'s decision, but may appeal.\r\n\r\nThe exact amount to be paid is expected to be finalised after AEG Live submits an amended list of its costs for items such as court filing fees and travel.','123',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-04-16 13:26:29','2014-04-16 14:34:35',NULL,4),(6,'first calculation of price','ln','ab','hs',21600,1,1,2,1,NULL,'first calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for pricefirst calculation for price','',1,0,'85.17.249.125:8089',1,'1',0,3,NULL,NULL,NULL,'2014-06-05 05:43:04','2014-06-21 21:15:37',NULL,7),(7,'Paper title','ln','es','ph',2073600,2,1,3,1,NULL,'Paper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper title','1',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 11:58:31','2014-06-06 14:31:03',NULL,7),(8,'paper 1 1','ln','es','co',2073600,1,1,3,1,NULL,'Paper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper title','1',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 11:59:25','2014-06-05 11:59:25',NULL,4),(9,'paper title','ln','es','co',2073600,1,1,3,1,NULL,'Paper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper titlePaper title','1',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 11:59:50','2014-06-05 12:00:56',NULL,7),(10,'esssay 1 p, 24+ deadline, 0 references MLA, double space','hs','es','hs',2073600,2,1,1,0,NULL,'esssay 1 p, 24+ deadline, 0 references MLA, double spaceesssay 1 p, 24+ deadline, 0 references MLA, double spaceesssay 1 p, 24+ deadline, 0 references MLA, double spaceesssay 1 p, 24+ deadline, 0 references MLA, double spaceesssay 1 p, 24+ deadline, 0 references MLA, double spaceesssay 1 p, 24+ deadline, 0 references MLA, double space','',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 12:05:02','2014-06-05 12:05:02',NULL,4),(11,'expensive essay','hs','cs','ph',21600,2,1,1,1,NULL,'expensive essayexpensive essayexpensive essayexpensive essayexpensive essayexpensive essayexpensive essayexpensive essayexpensive essayexpensive essay','',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 12:06:45','2014-06-05 12:06:45',NULL,4),(12,'3 days, 1 page, university','pa','re','un',259200,2,1,1,1,NULL,'3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university','1',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 12:17:48','2014-06-05 12:17:48',NULL,4),(13,'3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, univer','pa','re','un',259200,2,3,1,1,NULL,'3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university3 days, 1 page, university','',1,0,'customers.yourseller.net:8081',1,'1',0,7,NULL,NULL,NULL,'2014-06-05 12:19:34','2014-06-05 12:19:34',NULL,4),(14,'title','hs','re','hs',21600,1,2,2,2,NULL,'asd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkjasd lkj','',1,0,'customers.yourseller.net:8081',1,'1',0,3,NULL,NULL,NULL,'2014-06-09 09:41:37','2014-06-09 09:41:49',NULL,4),(15,'11111111111111111111111111111111','hs','es','co',21600,2,12,1,1,NULL,'11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111v','',1,0,'customers.yourseller.net:8081',1,'1',0,3,NULL,NULL,NULL,'2014-06-13 14:44:04','2014-06-21 20:32:50',NULL,7),(16,'11111111111111111111111111111111','hs','es','co',21600,2,1,1,1,NULL,'11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111v','1',1,0,'customers.yourseller.net:8081',1,'1',0,3,NULL,NULL,NULL,'2014-06-13 14:44:31','2014-06-20 05:56:55',NULL,7),(17,'222222','hs','10','hs',43200,1,2,1,2,NULL,'222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    222222222222222222222222222222    ','',1,0,'customers.yourseller.net:8081',1,'1',0,3,NULL,NULL,NULL,'2014-06-15 08:42:58','2014-06-20 05:05:35',NULL,7),(25,'3333333','hs','ab','hs',21600,1,2,1,2,NULL,'333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 ','',1,0,'customers.yourseller.net:8089',1,'1',0,3,NULL,NULL,NULL,'2014-06-17 06:27:26','2014-06-18 06:26:44',NULL,7),(26,'333333333333','hs','ab','hs',21600,1,3,1,3,NULL,'333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 333333 ','',1,0,'customers.yourseller.net:8089',1,'1',0,3,NULL,NULL,NULL,'2014-06-17 06:28:18','2014-06-18 06:46:29',NULL,7),(27,'sssssssssssssssssssssssssssss','hs','es','hs',2073600,2,1,1,1,NULL,'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss','1',1,0,'customers.yourseller.net:8081',1,'1',0,10,NULL,NULL,NULL,'2014-06-20 12:49:55','2014-06-20 12:54:37',NULL,4);
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
  `attach` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `fowner_id` int(11) NOT NULL,
  `ftask_id` int(11) NOT NULL,
  `access_level` varchar(1) COLLATE utf16_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `uploads_0455f6ba` (`fowner_id`),
  KEY `uploads_1c473884` (`ftask_id`),
  CONSTRAINT `fowner_id_refs_id_5d3b60be` FOREIGN KEY (`fowner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ftask_id_refs_id_51147dce` FOREIGN KEY (`ftask_id`) REFERENCES `tasks` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uploads`
--

LOCK TABLES `uploads` WRITE;
/*!40000 ALTER TABLE `uploads` DISABLE KEYS */;
INSERT INTO `uploads` VALUES (1,'2014-06-05 05:43:04','2014-06-05 05:43:04','customer/001_overview (3).pdf',3,6,'1'),(2,'2014-06-05 11:58:31','2014-06-05 11:58:31','Customer10/APA Style.doc',7,7,'1'),(3,'2014-06-05 11:59:50','2014-06-05 11:59:50','Customer10/APA Style_1.doc',7,9,'1'),(4,'2014-06-05 12:05:02','2014-06-05 12:05:02','Customer10/Chicago author-date sample.doc',7,10,'1'),(5,'2014-06-05 12:06:45','2014-06-05 12:06:45','Customer10/CONTRACT.doc',7,11,'1'),(6,'2014-06-09 09:41:38','2014-06-09 09:41:38','customer/001_overview (3)_1.pdf',3,14,'1'),(8,'2014-06-15 08:42:58','2014-06-15 08:42:58','customer/#9695137830 at the gate.-edited-remarks.doc',3,17,'1'),(9,'2014-06-17 06:27:26','2014-06-17 06:27:26','customer/002_overview.pdf',3,25,'1'),(10,'2014-06-17 06:28:18','2014-06-17 06:28:18','customer/002_overview_1.pdf',3,26,'1'),(11,'2014-06-20 12:49:55','2014-06-20 12:49:55','newscustomer12345/APA Style.doc',10,27,'1');
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
  `country` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `phone` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `site` varchar(100) COLLATE utf16_unicode_ci DEFAULT NULL,
  `updated` datetime NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  CONSTRAINT `user_ptr_id_refs_id_738769bc` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_profiles`
--

LOCK TABLES `user_profiles` WRITE;
/*!40000 ALTER TABLE `user_profiles` DISABLE KEYS */;
INSERT INTO `user_profiles` VALUES (1,1,'ua','123','customers.yourseller.com:8081','2014-04-15 14:30:00'),(2,0,'AT','1111','customers.yourseller.com:8081','2014-06-04 04:11:03'),(3,0,'AF','1111','customers.yourseller.com:8081','2014-04-15 12:32:00'),(4,0,'AF','1111','customers.yourseller.com:8081','2014-04-15 12:32:25'),(5,0,'AF','1111','customers.yourseller.com:8081','2014-04-15 12:32:55'),(6,0,'AF','123','customers.yourseller.com:8081','2014-04-15 15:11:26'),(7,0,'AF','123567','customers.yourseller.net:8081','2014-06-05 11:57:37'),(8,0,'AF','111111111111111111','customers.yourseller.net:8081','2014-06-19 19:16:30'),(9,0,'AF','111111111111111111','customers.yourseller.net:8081','2014-06-19 19:16:38'),(10,0,'AF','123','customers.yourseller.net:8081','2014-06-20 12:47:22');
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

-- Dump completed on 2014-06-21 23:19:56
