-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: repair
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add repair request',7,'add_repairrequest'),(26,'Can change repair request',7,'change_repairrequest'),(27,'Can delete repair request',7,'delete_repairrequest'),(28,'Can view repair request',7,'view_repairrequest'),(29,'Can add user profile',8,'add_userprofile'),(30,'Can change user profile',8,'change_userprofile'),(31,'Can delete user profile',8,'delete_userprofile'),(32,'Can view user profile',8,'view_userprofile'),(33,'Can add payment',9,'add_payment'),(34,'Can change payment',9,'change_payment'),(35,'Can delete payment',9,'delete_payment'),(36,'Can view payment',9,'view_payment'),(37,'Can add admin message',10,'add_adminmessage'),(38,'Can change admin message',10,'change_adminmessage'),(39,'Can delete admin message',10,'delete_adminmessage'),(40,'Can view admin message',10,'view_adminmessage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$1000000$p6ZQi4Ou1veMvPEqg4EdHq$givxXgRb+q/p7ic5khjnyPk/KL2lqyL6RoxNyot0irs=','2025-12-06 04:29:39.169734',0,'anji@gmail.com','anjitha','k','anji@gmail.com',0,1,'2025-12-02 11:28:24.452071'),(2,'pbkdf2_sha256$1000000$wLxLoTiISvdZwhSIOtPLXl$Hufd+yu21rU6SyuLBg5w/OACuMM7jcVur7pnaMWntJc=','2026-01-21 11:25:13.265226',1,'admin4','','','admin4@gmail.com',1,1,'2025-12-03 10:21:05.413521'),(3,'pbkdf2_sha256$1000000$uSDcnegy2hL47wA7V034y2$rlTSFYp6hsSpz3xAc9zStFRQj8B84YLbJdzLRSZHfic=','2025-12-30 06:24:36.514054',0,'tutu@gmail.com','tutu','v','tutu@gmail.com',0,1,'2025-12-29 04:43:06.758295'),(4,'pbkdf2_sha256$1000000$Z9HuqJhXIIW8g0VIPPr6Mo$GB3fv7hCpFfHJ5uROLWhiYVb/qCXQFnmEsaNZSYXb44=','2025-12-30 09:16:10.002931',1,'admin3','','','admin3@gmail.com',1,1,'2025-12-29 04:50:18.274628'),(5,'pbkdf2_sha256$1000000$DZ0hrkDY6TNrfVrJygHu5H$k7IUo/QinRPIt4348XK+aWSNJscD0T3zV2fZ/EX71lI=','2026-01-19 12:26:19.141520',0,'victer@gmail.com','victer','johney','victer@gmail.com',0,1,'2026-01-14 04:52:34.302560'),(6,'pbkdf2_sha256$1000000$8koP7Lyb0IWOJdRAfLjPKW$D+kLdZ9Ety0jJ4M87D4tUNkzYLZ2ckLixCNVB4XEdxY=','2026-01-19 12:23:02.050651',0,'vani@gmail.com','vani','r','vani@gmail.com',0,1,'2026-01-14 10:57:43.105796'),(7,'pbkdf2_sha256$1000000$l1aCwvJqTqtKySi9mViIwl$/Jxgc3PawOOnffdcLchvpntMk2zrUnpjTWDjGHyyBj4=','2026-01-21 11:29:31.887371',0,'s@gmail.com','sethu','y','s@gmail.com',0,1,'2026-01-19 12:27:06.550522');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'repairapp','adminmessage'),(9,'repairapp','payment'),(7,'repairapp','repairrequest'),(8,'repairapp','userprofile'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-12-02 11:27:37.345147'),(2,'auth','0001_initial','2025-12-02 11:27:38.593964'),(3,'admin','0001_initial','2025-12-02 11:27:38.822659'),(4,'admin','0002_logentry_remove_auto_add','2025-12-02 11:27:38.837647'),(5,'admin','0003_logentry_add_action_flag_choices','2025-12-02 11:27:38.859026'),(6,'contenttypes','0002_remove_content_type_name','2025-12-02 11:27:39.025556'),(7,'auth','0002_alter_permission_name_max_length','2025-12-02 11:27:39.172710'),(8,'auth','0003_alter_user_email_max_length','2025-12-02 11:27:39.239772'),(9,'auth','0004_alter_user_username_opts','2025-12-02 11:27:39.251568'),(10,'auth','0005_alter_user_last_login_null','2025-12-02 11:27:39.359528'),(11,'auth','0006_require_contenttypes_0002','2025-12-02 11:27:39.363531'),(12,'auth','0007_alter_validators_add_error_messages','2025-12-02 11:27:39.376542'),(13,'auth','0008_alter_user_username_max_length','2025-12-02 11:27:39.473138'),(14,'auth','0009_alter_user_last_name_max_length','2025-12-02 11:27:39.565449'),(15,'auth','0010_alter_group_name_max_length','2025-12-02 11:27:39.596632'),(16,'auth','0011_update_proxy_permissions','2025-12-02 11:27:39.615635'),(17,'auth','0012_alter_user_first_name_max_length','2025-12-02 11:27:39.707129'),(18,'repairapp','0001_initial','2025-12-02 11:27:40.037236'),(19,'sessions','0001_initial','2025-12-02 11:27:40.139082'),(20,'repairapp','0002_repairrequest_attempted_solutions_and_more','2025-12-03 06:38:00.147937'),(21,'repairapp','0003_repairrequest_completed_date','2025-12-06 06:01:43.117820'),(22,'repairapp','0004_payment','2026-01-16 04:22:00.570731'),(23,'repairapp','0005_alter_repairrequest_service_type_adminmessage','2026-01-16 06:52:36.336020'),(24,'repairapp','0006_adminmessage_pickup_charge_and_more','2026-01-20 07:28:17.150385'),(25,'repairapp','0007_remove_payment_amount_payment_pickup_charge_and_more','2026-01-20 13:02:31.265864');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2073u1gbminv2ih9z2qs1bwu489zyi2s','.eJxVjMsOwiAUBf-FtSGAUKhL9_0GcrkPqZo2Ke3K-O_apAvdnpk5L5VhW2veGi95JHVRQZ1-twL44GkHdIfpNmucp3UZi94VfdCmh5n4eT3cv4MKrX5rBwWdD1J6jp24RJhCoGiQfOgdgrEdFUGW2FvH1iQg7z2K2LMXJ6zeHwITOMc:1vft4R:g7d81BO7w2eGDo5t_01BApgfn-5Ti5fIVo1P6kNujVg','2026-01-28 05:05:27.626735'),('2700lpu4ug9lmmkdaumwrt6b50s2lfg0','.eJxVjEEOwiAQAP_C2RC6tJT26N03kGVZLWrAQJtojH83JD3odWYyb-FwWxe3VS4uBjELEIdf5pFunJoIV0yXLCmntUQvWyJ3W-UpB74f9_ZvsGBd2hYM9SYo7mAazoOaVI9GW981CqBQ21ExaLYjEoOBASmEzkLwutdEbVq51piT4-cjlpeY1ecLWJQ-lA:1vfzEN:t2A_yhpBwMChg_uyp8qFuWjW-8MbY9htTNv43CdNKAU','2026-01-28 11:40:07.677084'),('4mg26ba8ty72fql7ppagzbuf3t2hf6sf','.eJxVjMsOwiAUBf-FtSGAUKhL9_0GcrkPqZo2Ke3K-O_apAvdnpk5L5VhW2veGi95JHVRQZ1-twL44GkHdIfpNmucp3UZi94VfdCmh5n4eT3cv4MKrX5rBwWdD1J6jp24RJhCoGiQfOgdgrEdFUGW2FvH1iQg7z2K2LMXJ6zeHwITOMc:1vhmnH:VH4TDfrFao4L1zQHOfFBXdy2Rkc-1lqrpcOf1rpQBOU','2026-02-02 10:47:35.422625'),('521izqf146s761mjlnpqsav8dw2kq20c','.eJxVjMsOwiAQRf-FtSG8p7h07zeQYQCpGkhKuzL-uzbpQrf3nHNfLOC21rCNvIQ5sTMDdvrdItIjtx2kO7Zb59TbusyR7wo_6ODXnvLzcrh_BxVH_dZFOgLnhc2ejEFdSPlMxRhtJyMKeR9lSqBAWuckWEUZjC6uRNSTkJq9P9xQN1o:1viWOx:r9i7srbh1Qznn_WcWop1s7xfc-gM3zlrA2i8rT-Hcd0','2026-02-04 11:29:31.894376'),('6tv96cknkmrx38k6yk0d4opq178z0xfu','.eJxVjssKwjAURP8lawnN-94u3fsNIa_aqCTStKCI_24rXSjMaubMMC9i3TKPdmlpsjmSnnBy-PW8C9dUtiBeXDlXGmqZp-zphtA9bfRUY7odd_ZvYHRtXNssCtAqcO4BwEejDRPCKe8HwbQcUEqhDGDskEmOYDCtgsAHg6gVfl-11FquxabHPU9P0nfvD0D7PZ4:1vfwAC:32VyCV111wjSK0AfxdEj4rCRPONRFpFOf5vaK1XYL4s','2026-01-28 08:23:36.752093'),('7am73q3j3na5ale8gjcs4016y1n5wlrg','.eJxVjEEOgjAQRe_StWkq06HFpXvO0MwwU0ENTSisjHdXEha6_e-9_zKJtnVMW9UlTWIuBszpd2MaHjrvQO4034odyrwuE9tdsQetti-iz-vh_h2MVMdvzaKCAA65BYSzNNxBp9T6GISJRBScbyC6zqFwJMwegV0eIEPwQc37A-nkN_k:1va5sj:Y3BlrA0BxIrnUIZMi5cB1y9HYO8T3E4RVYbjYivVGXc','2026-01-12 05:33:25.841785'),('9s1778thocccm7jmow5ubb7nusx5xncb','.eJxVjMsOwiAUBf-FtSGAUKhL9_0GcrkPqZo2Ke3K-O_apAvdnpk5L5VhW2veGi95JHVRQZ1-twL44GkHdIfpNmucp3UZi94VfdCmh5n4eT3cv4MKrX5rBwWdD1J6jp24RJhCoGiQfOgdgrEdFUGW2FvH1iQg7z2K2LMXJ6zeHwITOMc:1vgf3N:Uv_Crtu_cjGuxd7LspP1SQMbfZUQ_3ItCfi4U9E2E_4','2026-01-30 08:19:33.845809'),('eq7qdxo7qiwi5v8cpg5mbozrb0bvojan','.eJxVjEEOwiAQRe_C2hCgDBSX7j0DmWGoVA0kpV0Z765NutDtf-_9l4i4rSVuPS9xZnEWWpx-N8L0yHUHfMd6azK1ui4zyV2RB-3y2jg_L4f7d1Cwl28NdmANVpMfbLCObHKUHUHGAMpxssYFBTwQTaPPBhEnDUTJGzWSVyzeH9IXN_Q:1vRjvP:pSQKmXqsYYngSTueaE6-tQjdpbqnolcOul5VXMBgJog','2025-12-20 04:29:39.180768'),('hybwmu1mv4rvt1lsqp6jsfqr8fwl1psv','.eJxVjEEOwiAQAP_C2RC6tJT26N03kGVZLWrAQJtojH83JD3odWYyb-FwWxe3VS4uBjELEIdf5pFunJoIV0yXLCmntUQvWyJ3W-UpB74f9_ZvsGBd2hYM9SYo7mAazoOaVI9GW981CqBQ21ExaLYjEoOBASmEzkLwutdEbVq51piT4-cjlpeY1ecLWJQ-lA:1vgiEp:gzUo6YD5FNgNdWPbpymv2b7WdVvu6arQRDdNkhjOqG8','2026-01-30 11:43:35.280568'),('lwo50il3hpvv4a1fsfti47gp16gppz19','.eJxVjMsOwiAUBf-FtSGAUKhL9_0GcrkPqZo2Ke3K-O_apAvdnpk5L5VhW2veGi95JHVRQZ1-twL44GkHdIfpNmucp3UZi94VfdCmh5n4eT3cv4MKrX5rBwWdD1J6jp24RJhCoGiQfOgdgrEdFUGW2FvH1iQg7z2K2LMXJ6zeHwITOMc:1vgbEE:ouYLqtqzyrd5uufTAM_oUsKc13m23tcJ9qk1Wmke_AU','2026-01-30 04:14:30.482846'),('p7hyy5ujbrgb6cwy0wucle45b2eq9var','.eJxVjEEOwiAQRe_C2hDKtEC6dO8ZyDADFjVgSptojHfXJl3o9r_330t4XJfJry3OPrMYRS8Ov1tAusayAb5gOVdJtSxzDnJT5E6bPFWOt-Pu_gUmbNP3DVYR9Iado4ECJuqCJVAJNSflWBnAATho1w1grVUWe2Nc1KBVAKPTFm2xtVyLj497np9iVO8PhKk-oA:1vaVpq:mv-WdYOtNfwN9GhzLEkNPn-jukw8mrH5n5BBBiVFOl8','2026-01-13 09:16:10.014933'),('s2tl01565akf7facif9ey1iydymm54nw','.eJxVjssKwjAURP8lawnN-94u3fsNIa_aqCTStKCI_24rXSjMaubMMC9i3TKPdmlpsjmSnnBy-PW8C9dUtiBeXDlXGmqZp-zphtA9bfRUY7odd_ZvYHRtXNssCtAqcO4BwEejDRPCKe8HwbQcUEqhDGDskEmOYDCtgsAHg6gVfl-11FquxabHPU9P0nfvD0D7PZ4:1vQjzI:2i6r6MqE9PCfmOQ9KWbBoerBJlfqQypGg_a_RhGgBMg','2025-12-17 10:21:32.333338'),('xca5orfr3gg1ca771bh18rgpyxzc02xm','.eJxVjssKwjAURP8lawnN-94u3fsNIa_aqCTStKCI_24rXSjMaubMMC9i3TKPdmlpsjmSnnBy-PW8C9dUtiBeXDlXGmqZp-zphtA9bfRUY7odd_ZvYHRtXNssCtAqcO4BwEejDRPCKe8HwbQcUEqhDGDskEmOYDCtgsAHg6gVfl-11FquxabHPU9P0nfvD0D7PZ4:1vTYlt:Ofb1Lmng6rax9AHUXP0Gj4c9B5eTdzzxFAnfB0NwT8A','2025-12-25 04:59:21.719080');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairapp_adminmessage`
--

DROP TABLE IF EXISTS `repairapp_adminmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairapp_adminmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `repair_request_id` bigint NOT NULL,
  `pickup_charge` decimal(10,2) DEFAULT NULL,
  `repair_charge` decimal(10,2) NOT NULL,
  `tax` decimal(10,2) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `repairapp_adminmessa_repair_request_id_99ee78b7_fk_repairapp` (`repair_request_id`),
  CONSTRAINT `repairapp_adminmessa_repair_request_id_99ee78b7_fk_repairapp` FOREIGN KEY (`repair_request_id`) REFERENCES `repairapp_repairrequest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairapp_adminmessage`
--

LOCK TABLES `repairapp_adminmessage` WRITE;
/*!40000 ALTER TABLE `repairapp_adminmessage` DISABLE KEYS */;
INSERT INTO `repairapp_adminmessage` VALUES (1,'hi....repairs are done ..please pay the amount','2026-01-16 11:44:58.562876',3,NULL,0.00,0.00,0.00),(2,'hi,\r\nservice has been done.','2026-01-19 10:59:12.956065',4,NULL,0.00,0.00,0.00),(15,'done..ok\r\n        \r\n        \r\n        ','2026-01-21 09:18:04.814193',6,45.00,850.00,34.00,929.00);
/*!40000 ALTER TABLE `repairapp_adminmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairapp_payment`
--

DROP TABLE IF EXISTS `repairapp_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairapp_payment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `admin_note` longtext,
  `payment_status` varchar(20) NOT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `transaction_id` varchar(100) DEFAULT NULL,
  `paid_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `repair_request_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `pickup_charge` decimal(10,2) NOT NULL,
  `repair_charge` decimal(10,2) NOT NULL,
  `tax` decimal(10,2) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repair_request_id` (`repair_request_id`),
  KEY `repairapp_payment_user_id_c9b9b75b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `repairapp_payment_repair_request_id_81c5c621_fk_repairapp` FOREIGN KEY (`repair_request_id`) REFERENCES `repairapp_repairrequest` (`id`),
  CONSTRAINT `repairapp_payment_user_id_c9b9b75b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairapp_payment`
--

LOCK TABLES `repairapp_payment` WRITE;
/*!40000 ALTER TABLE `repairapp_payment` DISABLE KEYS */;
INSERT INTO `repairapp_payment` VALUES (2,NULL,'paid','card',NULL,'2026-01-21 11:18:50.394230','2026-01-21 09:37:58.030332','2026-01-21 11:18:50.394230',6,7,45.00,850.00,34.00,929.00);
/*!40000 ALTER TABLE `repairapp_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairapp_repairrequest`
--

DROP TABLE IF EXISTS `repairapp_repairrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairapp_repairrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `device_type` varchar(50) NOT NULL,
  `device_brand` varchar(100) NOT NULL,
  `device_model` varchar(100) NOT NULL,
  `problem_description` longtext NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `attempted_solutions` longtext,
  `contact_method` varchar(50) DEFAULT NULL,
  `data_backup` tinyint(1) NOT NULL,
  `diagnostic_only` tinyint(1) NOT NULL,
  `estimated_budget` int DEFAULT NULL,
  `problem_battery` tinyint(1) NOT NULL,
  `problem_frequency` varchar(50) DEFAULT NULL,
  `problem_hardware` tinyint(1) NOT NULL,
  `problem_internet` tinyint(1) NOT NULL,
  `problem_keyboard` tinyint(1) NOT NULL,
  `problem_other` tinyint(1) NOT NULL,
  `problem_screen` tinyint(1) NOT NULL,
  `problem_software` tinyint(1) NOT NULL,
  `problem_sound` tinyint(1) NOT NULL,
  `problem_start_date` date DEFAULT NULL,
  `problem_virus` tinyint(1) NOT NULL,
  `purchase_date` date DEFAULT NULL,
  `serial_number` varchar(100) DEFAULT NULL,
  `service_type` varchar(20) NOT NULL,
  `special_instructions` longtext,
  `urgency_level` varchar(20) DEFAULT NULL,
  `completed_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `repairapp_repairrequest_user_id_e71e5e41_fk_auth_user_id` (`user_id`),
  CONSTRAINT `repairapp_repairrequest_user_id_e71e5e41_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairapp_repairrequest`
--

LOCK TABLES `repairapp_repairrequest` WRITE;
/*!40000 ALTER TABLE `repairapp_repairrequest` DISABLE KEYS */;
INSERT INTO `repairapp_repairrequest` VALUES (1,'laptop','dell','test','fg','completed','2025-12-03 05:13:37.895798','2026-01-19 12:40:54.522368',1,NULL,NULL,0,0,NULL,0,NULL,0,0,0,0,0,0,0,NULL,0,NULL,NULL,'shop',NULL,NULL,NULL),(2,'desktop','hp','test','test','in_progress','2025-12-03 06:48:59.685584','2025-12-05 11:05:01.738373',1,'no','phone',1,0,1200,0,'always',0,0,0,0,1,0,0,'2025-12-03',0,'2024-12-03','56465','onsite',NULL,'high',NULL),(3,'laptop','dell','test','testt','completed','2025-12-29 04:45:16.901714','2026-01-14 05:01:29.847803',3,'no','phone',1,0,2000,0,'sometimes',0,0,1,0,0,0,0,'2025-12-29',0,'2024-12-29','56465','onsite',NULL,'high',NULL),(4,'laptop','dell','vostro14300','battery issue','completed','2026-01-14 04:56:13.010667','2026-01-14 05:04:57.053393',5,'df','whatsapp',0,1,5550,0,'sometimes',0,0,0,0,0,0,1,'2026-01-06',0,'2025-01-05','1345','pickup',NULL,'low',NULL),(5,'laptop','dell','vostro14300','scdv vc c','completed','2026-01-14 11:08:12.342825','2026-01-19 12:13:57.476379',6,'yes','whatsapp',0,0,1500,0,'sometimes',1,0,0,0,0,0,0,'2026-01-14',0,'2025-01-01','1345','onsite',NULL,'high',NULL),(6,'desktop','dell','vostro14300','test','completed','2026-01-19 12:28:47.280534','2026-01-21 10:51:47.937751',7,'no','phone',0,0,2000,0,'always',1,0,0,0,0,0,0,'2026-01-19',0,'2025-01-18','56465','pickup',NULL,'high',NULL);
/*!40000 ALTER TABLE `repairapp_repairrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repairapp_userprofile`
--

DROP TABLE IF EXISTS `repairapp_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repairapp_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone` varchar(15) DEFAULT NULL,
  `address` longtext,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `repairapp_userprofile_user_id_a98066be_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repairapp_userprofile`
--

LOCK TABLES `repairapp_userprofile` WRITE;
/*!40000 ALTER TABLE `repairapp_userprofile` DISABLE KEYS */;
INSERT INTO `repairapp_userprofile` VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,'','2025-12-03 06:51:34.608683','2025-12-03 06:51:34.608683',1),(2,'9632589652','tuttu nte veed','tuttu city','kerala','698568','india','profile_pictures/user_3_goku.jpeg','2025-12-29 04:45:48.747692','2025-12-30 07:17:44.604507',3),(3,'9875845625','victer villa','mannanam','kerala','689562','India','profile_pictures/user_5_goku.jpeg','2026-01-14 04:56:34.666935','2026-01-19 10:54:10.548747',5),(4,'9865432118','kottayam','kottayam','kerala','6985632','india','profile_pictures/user_6_anji.jpeg','2026-01-14 11:08:31.709826','2026-01-14 11:11:31.481829',6),(5,NULL,NULL,NULL,NULL,NULL,NULL,'','2026-01-20 04:49:07.811533','2026-01-20 04:49:07.811533',7);
/*!40000 ALTER TABLE `repairapp_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-01-21 17:02:28
