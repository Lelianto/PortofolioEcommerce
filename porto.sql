-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: porto
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.18.04.4

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('c414973aa81f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `book` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `judul` varchar(255) NOT NULL,
  `penulis` varchar(255) NOT NULL,
  `jumlah_halaman` int(11) NOT NULL,
  `tanggal_terbit` varchar(255) NOT NULL,
  `isbn` varchar(50) NOT NULL,
  `genre` varchar(255) NOT NULL,
  `bahasa` varchar(255) NOT NULL,
  `berat` float NOT NULL,
  `lebar` float NOT NULL,
  `panjang` int(11) NOT NULL,
  `jenis_cover` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `foto_buku` varchar(255) NOT NULL,
  `sinopsis` varchar(10000) NOT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `penerbit` varchar(10000) NOT NULL,
  `email_user` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `isbn` (`isbn`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Konspirasi Alam Semesta','Fiersa Besari',220,'10/2016','192310924124','Komedi','Indonesia',0.25,0,0,'Soft Cover','Ready Stock','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg','Melakukan bebas dengan terbatas',75000,84,2,'Gramedia','garry@alterra.id'),(3,'Bahasa Matematika','Lelianto Pradana',155,'10/2019','192310921239','Romantis','Indonesia',0.25,0,0,'Soft Cover','Pre-Order','https://www.canva.com/id_id/belajar/wp-content/uploads/sites/13/2018/02/thelightbetweenoceans-tb-728x0-1-tb-800x0.jpg','Melakukan bebas dengan terbatas',55000,0,2,'Gramedia','garry@alterra.id'),(4,'Celetuk','Willy Sumarno',100,'11/2019','192381249129','Antologi Puisi','Indonesia',0.25,15,0,'Soft Cover','Pre-Order','https://upload.wikimedia.org/wikipedia/id/8/89/Sang_Pemimpi_sampul.jpg','Melakukan bebas dengan terbatas',40000,0,3,'Mizan Store','willy@alterra.id'),(12,'Senyummu Tenggelam','Lelianto Eko Pradana',323,'15-12-2017','0328028209181','Romantis','Bahasa Indonesia',0.223,15,30,'Soft Cover','Ready Stock','https://ebooks.gramedia.com/ebook-covers/42171/image_highres/ID_HU2018MTH04HU.jpg','Kamu, untuk semua sikap baikmu dan semua perhatian kecilmu tak ingin aku menganggapnya lebih. Aku tak ingin berada dalam lingkaran kebaperan yang ku anggap tidak berguna. Sesekali aku merasa sangat dekat denganmu, perhatian dan leluconmu membuatku sangat nyaman jika berada di dekatmu. Terlebih pembawaan dirimu yang jauh lebih tenang dan dewasa dibanding denganku. Kau paham kapan harus berbicara serius dan kapan kau harus bertingkah konyol, kamu untuk semua sikap baikmu dan semua perhatian kecilmu tak ingin aku menganggapnya lebih.',85000,100,7,'Mizan Store','lusiana@alterra.id'),(13,'Berjalan di Atas Cahaya','Hanum Salsabiela',333,'05-12-2015','111222333444','Teenlit','Bahasa Indonesia',0.2,15,29,'Soft Cover','Ready Stock','https://www.dakwatuna.com/wp-content/uploads/2014/07/cover-buku-berjalan-di-atas-cahaya.jpg','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',65000,96,10,'Gramedia','lelianto.pradana@gmail.com'),(14,'Pergi','Tere Liye',234,'05-10-2016','222333444555','Drama','Bahasa Indonesia',0.223,14.5,30,'Soft Cover','Pre-Order','https://togamas.com/css/images/items/potrait/muri_6469_Pergi__New_Cover___.jpg\n','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',56000,100,10,'Gramedia','lelianto.pradana@gmail.com'),(15,'Enchantment','Guy Kawasaki',235,'20-02-2019','333444555666','Sejarah','Bahasa Inggris',0.123,15,28,'Soft Cover','Ready Stock','https://blog.sribu.com/wp-content/uploads/2018/07/Cover-Buku-Minimalis-673x1024.jpg\n','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',75000,100,10,'Mizan Store','lelianto.pradana@gmail.com'),(16,'Bulan','Tere Liye',454,'15-02-2017','444555666777','Misteri','Bahasa Indonesia',0.223,14,29,'Soft Cover','Pre-Order','https://ecs7.tokopedia.net/img/cache/700/product-1/2018/9/28/4162462/4162462_0d70c72e-0d25-42b7-8bc9-f7ca9bcef9e8.jpg\n','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',47000,100,10,'Gramedia','lelianto.pradana@gmail.com'),(17,'Bara','Febriardi R.',345,'15-01-2018','444333222111','Fantasi','Bahasa Indonesia',0.251,14,30,'Soft Cover','Ready Stock','https://ssvr.bukukita.com/babacms/displaybuku/101400_f.jpg\n','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',75000,0,11,'Mizan Store','lelianto99@yahoo.co.id'),(18,'Laskar Pelangi','Andrea Hirata',456,'03-05-2014','999888777333','Petualangan','Bahasa Indonesia',0.2,14,28,'Soft Cover','Pre-Order','https://upload.wikimedia.org/wikipedia/id/8/8e/Laskar_pelangi_sampul.jpg','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',56000,0,11,'Gramedia','lelianto99@yahoo.co.id'),(19,'After Atlas','Emma Newman',432,'15-12-2013','777666558558','Drama','Bahasa Indonesia',0.28,14.5,30,'Soft Cover','Pre-Order','https://blog.sribu.com/wp-content/uploads/2018/07/Nuansa-Cover-Buku.jpg','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',85000,0,11,'Republika','lelianto99@yahoo.co.id'),(20,'Pengabdi Cilok','Iwok Abqary & Irvan Aqila',333,'05-12-2015','21848124712712391981','Komedi','Bahasa Indonesia',0.254,15,28,'Soft Cover','Ready Stock','https://cdn.qubicle.id/images/2018/05/04/675b7dc822033b0ea0b4c3ea41c8f171.jpg','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC \"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',65000,100,11,'Republika','lelianto99@yahoo.co.id'),(21,'Perahu Kertas','Dee Lestari',362,'01-01-2016','876565434321232','Fan-Fiction','Bahasa Indonesia',0.251,15,30,'Soft Cover','Pre-Order','https://upload.wikimedia.org/wikipedia/id/7/7f/Perahu_Kertas_Sampul.jpg\n','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\n\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',56000,100,7,'Republika','lusiana@alterra.id'),(22,'Rindu','Tere Liye',251,'02-01-2019','983721928319245234','Sejarah','Bahasa Indonesia',0.2,15,29,'Soft Cover','Ready Stock','https://inc.mizanstore.com/aassets/img/com_cart/produk/covPAB-014.jpg','The standard Lorem Ipsum passage, used since the 1500s\n\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\"\n\nSection 1.10.32 of \"de Finibus Bonorum et Malorum\", written by Cicero in 45 BC\n\"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?\"',65000,100,7,'Mizan Store','lusiana@alterra.id'),(23,'Bumi Cinta','Habiburahman El Shirazy',234,'25-12-2015','283028349234873','Songlit','Bahasa Indonesia',0.251,14.5,26,'Soft Cover','Pre-Order','https://inc.mizanstore.com/aassets/img/com_cart/produk/bumi-cinta-habiburahman-el-shirazy.jpg','You can design and manage all your transactional templates in Passport, our email design tool. All gathered in one single library, your templates can be sent easily through our SMTP or Send API thanks to their unique ID. You can design and manage all your transactional templates in Passport, our email design tool. All gathered in one single library, your templates can be sent easily through our SMTP or Send API thanks to their unique ID. You can design and manage all your transactional templates in Passport, our email design tool. All gathered in one single library, your templates can be sent easily through our SMTP or Send API thanks to their unique ID.',58000,0,9,'Gramedia','lelianto.eko@gmail.com');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `judul` varchar(255) NOT NULL,
  `penulis` varchar(255) NOT NULL,
  `jenis_cover` varchar(255) NOT NULL,
  `foto_buku` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `status_cart` tinyint(1) DEFAULT NULL,
  `book_id` int(11) DEFAULT NULL,
  `berat` float NOT NULL,
  `status_jual` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE,
  CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (11,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(13,9,'Bahasa Matematika','Lelianto Pradana','Soft Cover','https://www.canva.com/id_id/belajar/wp-content/uploads/sites/13/2018/02/thelightbetweenoceans-tb-728x0-1-tb-800x0.jpg',55000,1,'lelianto.eko@gmail.com',1,3,0.25,'Pre-Order'),(14,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(15,9,'Bahasa Matematika','Lelianto Pradana','Soft Cover','https://www.canva.com/id_id/belajar/wp-content/uploads/sites/13/2018/02/thelightbetweenoceans-tb-728x0-1-tb-800x0.jpg',55000,1,'lelianto.eko@gmail.com',1,3,0.25,'Pre-Order'),(16,9,'Celetuk','Willy Sumarno','Soft Cover','https://upload.wikimedia.org/wikipedia/id/8/89/Sang_Pemimpi_sampul.jpg',40000,1,'lelianto.eko@gmail.com',1,4,0.25,'Pre-Order'),(17,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(19,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(21,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(22,9,'Bahasa Matematika','Lelianto Pradana','Soft Cover','https://www.canva.com/id_id/belajar/wp-content/uploads/sites/13/2018/02/thelightbetweenoceans-tb-728x0-1-tb-800x0.jpg',55000,1,'lelianto.eko@gmail.com',1,3,0.25,'Pre-Order'),(23,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(29,7,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,3,'lusiana@alterra.id',1,1,0.25,'Ready Stock'),(32,7,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,3,'lusiana@alterra.id',1,1,0.25,'Ready Stock'),(33,7,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lusiana@alterra.id',1,1,0.25,'Ready Stock'),(35,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,3,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(46,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,2,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(111,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,4,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(113,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(114,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(115,9,'Berjalan di Atas Cahaya','Hanum Salsabiela','Soft Cover','https://www.dakwatuna.com/wp-content/uploads/2014/07/cover-buku-berjalan-di-atas-cahaya.jpg',65000,4,'lelianto.eko@gmail.com',1,13,0.2,'Ready Stock'),(116,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',1,1,0.25,'Ready Stock'),(119,9,'Konspirasi Alam Semesta','Fiersa Besari','Soft Cover','https://ssvr.bukukita.com/babacms/displaybuku/94832_f.jpg',75000,1,'lelianto.eko@gmail.com',0,1,0.25,'Ready Stock');
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_id` int(11) DEFAULT NULL,
  `nama_jalan` varchar(255) NOT NULL,
  `rt_rw` varchar(255) NOT NULL,
  `kelurahan` varchar(255) NOT NULL,
  `kecamatan` varchar(255) NOT NULL,
  `kota_kabupaten` varchar(255) NOT NULL,
  `provinsi` varchar(255) NOT NULL,
  `kode_pos` varchar(255) NOT NULL,
  `nomor_telepon` varchar(255) NOT NULL,
  `ongkir` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_id` (`cart_id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (1,NULL,'None','None','None','None','Jakarta','None','None','None',0),(2,NULL,'None','None','None','None','Jakarta','None','None','None',0),(3,NULL,'None','None','None','None','Jakarta','None','None','None',0),(4,NULL,'None','None','None','None','Jakarta','None','None','None',0),(5,NULL,'None','None','None','None','Jakarta','None','None','None',0),(6,NULL,'None','None','None','None','Jakarta','None','None','None',0),(7,NULL,'None','None','None','None','Jakarta','None','None','None',0),(8,NULL,'None','None','None','None','Jakarta','None','None','None',0),(9,NULL,'None','None','None','None','Jakarta','None','None','None',0),(10,NULL,'None','None','None','None','Jakarta','None','None','None',0),(11,NULL,'None','None','None','None','Jakarta','None','None','None',0),(12,NULL,'None','None','None','None','Jakarta','None','None','None',0),(13,NULL,'None','None','None','None','Jakarta','None','None','None',0),(14,NULL,'None','None','None','None','Jakarta','None','None','None',0),(15,NULL,'None','None','None','None','Bandung','None','None','None',0),(16,NULL,'None','None','None','None','Bandung','None','None','None',0),(17,NULL,'None','None','None','None','Bandung','None','None','None',0),(18,NULL,'None','None','None','None','Bandung','None','None','None',0),(19,NULL,'None','None','None','None','Bandung','None','None','None',0),(20,NULL,'None','None','None','None','Bandung','None','None','None',0),(21,NULL,'None','None','None','None','Bandung','None','None','None',0),(22,NULL,'None','None','None','None','Depok','None','None','None',0),(23,NULL,'None','None','None','None','Medan','None','None','None',0),(24,NULL,'None','None','None','None','Medan','None','None','None',0),(25,NULL,'None','None','None','None','Medan','None','None','None',0),(26,NULL,'None','None','None','None','Depok','None','None','None',0),(27,NULL,'None','None','None','None','Depok','None','None','None',0),(28,NULL,'None','None','None','None','Boyolali','None','None','None',57000),(29,NULL,'None','None','None','None','Depok','None','None','None',54000),(30,NULL,'None','None','None','None','Depok','None','None','None',54000),(31,NULL,'Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','0129381283',21000),(32,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','081524243535','65115','None',21000),(33,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','None',21000),(34,NULL,'None','None','None','None','Malang','None','None','None',21000),(35,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','081276123615','65115','None',21000),(36,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','0817263528237','65115','None',21000),(37,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','None',21000),(38,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','082524235676','65115','None',21000),(39,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Depok','028232726327','16424','None',60000),(40,NULL,'None','None','None','None','Malang','None','None','None',35000),(41,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Klaten','081292832928','65115','None',80000),(42,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Medan','081524236474','65115','None',252000),(43,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Semarang','09128312738123','65115','None',84000),(44,NULL,'None','None','None','None','Malang','None','None','None',49000),(45,NULL,'None','None','None','None','Malang','None','None','None',49000),(46,NULL,'None','None','None','None','Malang','None','None','None',56000),(47,NULL,'None','None','None','None','Malang','None','None','None',56000),(48,NULL,'None','None','None','None','Depok','081524235654','None','None',120000),(49,NULL,'None','None','None','None','Malang','None','None','None',70000),(50,NULL,'None','None','None','None','Boyolali','None','None','None',176000),(51,NULL,'None','None','None','None','Depok','None','None','None',135000),(52,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','0815263252763','65115','',77000),(53,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','0815263252763','65115','',77000),(54,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','','','',77000),(55,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','','','',77000),(56,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','','',77000),(57,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','',77000),(58,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','08152424242424','65115','',77000),(59,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','0815242424','65115','',77000),(60,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','',77000),(61,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','08162317123','65115','',77000),(62,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','081123453456',77000),(63,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','081123453456',77000),(64,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','081526242625',42000),(65,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','081123453456',49000),(66,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','085637627367',56000),(67,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','085637627367',56000),(68,NULL,'Jalan Tidar','01/07','Tidar','Karangbesuki','Malang','Jawa Timur','65115','085637627367',63000);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_confirm`
--

DROP TABLE IF EXISTS `payment_confirm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment_confirm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_biaya` int(11) NOT NULL,
  `nomor_pemesanan` varchar(255) NOT NULL,
  `tanggal_pemesanan` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_confirm`
--

LOCK TABLES `payment_confirm` WRITE;
/*!40000 ALTER TABLE `payment_confirm` DISABLE KEYS */;
INSERT INTO `payment_confirm` VALUES (1,54000,'D9F2A7BAF3','04/01/2020, 21:54:37'),(2,54000,'D9F2A7BAF3','04/01/2020, 23:06:00'),(3,54000,'D9F2A7BAF3','04/01/2020, 23:14:33'),(4,54000,'D9F2A7BAF3','04/01/2020, 23:30:44'),(5,887000,'D9F2A7BAF3','04/01/2020, 23:38:02'),(6,54000,'D9F2A7BAF3','04/01/2020, 23:41:30'),(7,54000,'D9F2A7BAF3','04/01/2020, 23:42:37'),(8,54000,'D9F2A7BAF3','04/01/2020, 23:45:59'),(9,54000,'D9F2A7BAF3','04/01/2020, 23:46:29'),(10,54000,'D9F2A7BAF3','04/01/2020, 23:50:08'),(11,887000,'D9F2A7BAF3','04/01/2020, 23:50:50'),(12,54000,'D9F2A7BAF3','04/01/2020, 23:56:55'),(13,54000,'D9F2A7BAF3','04/01/2020, 23:58:01'),(14,54000,'D9F2A7BAF3','04/01/2020, 23:58:50'),(15,54000,'D9F2A7BAF3','05/01/2020, 00:00:36'),(16,887000,'D9F2A7BAF3','05/01/2020, 00:01:56'),(17,473000,'D0297E236D','13/01/2020, 12:04:31'),(18,221000,'D0297E236D','13/01/2020, 12:08:49'),(19,196000,'E6D163E820','13/01/2020, 17:23:25'),(20,296000,'B97FC2AF39','13/01/2020, 20:44:44'),(21,422000,'5BADE97BAF','13/01/2020, 21:24:54'),(22,245000,'D2299F6D23','13/01/2020, 21:26:20'),(23,124000,'8FFABDFFC4','13/01/2020, 21:28:42'),(24,265000,'5886680CB9','13/01/2020, 21:29:47'),(25,131000,'C7D8B9AACD','13/01/2020, 21:32:34'),(26,122000,'43881C655F','13/01/2020, 23:55:43'),(27,517000,'AC9128303F','14/01/2020, 20:18:55'),(28,292000,'AC9128303F','14/01/2020, 20:18:55'),(29,70000,'3B5C6E0B01','14/01/2020, 21:50:12'),(30,553000,'3B5C6E0B01','14/01/2020, 21:50:12'),(31,681000,'F613F563BD','14/01/2020, 21:52:01'),(32,618000,'3D585E4C22','15/01/2020, 17:08:08'),(33,227000,'A6E1B9770F','17/01/2020, 10:38:38'),(34,342000,'9D7B701668','17/01/2020, 22:43:22'),(35,124000,'D4C9EC6997','17/01/2020, 23:09:42'),(36,131000,'CE92BF5ADD','17/01/2020, 23:51:07'),(37,316000,'8708677C48','18/01/2020, 08:35:53'),(38,138000,'003946C48F','18/01/2020, 12:22:07');
/*!40000 ALTER TABLE `payment_confirm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_lengkap` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `kata_sandi` varchar(255) NOT NULL,
  `tanggal_lahir` varchar(10) DEFAULT NULL,
  `nomor_telepon` varchar(15) DEFAULT NULL,
  `foto_profil` varchar(500) DEFAULT NULL,
  `genre` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (2,'Garry','garry@alterra.id','25d55ad283aa400af464c76d713c07ad','01/01/1996','0123456789012','Image.jpg','Action'),(3,'Willy Sumarno','willy@alterra.id','5e8667a439c68f5145dd2fcbecf02209','01/02/1995',NULL,NULL,NULL),(7,'Lusiana','lusiana@alterra.id','7cf99eed6b2efda8fb8c982d8a6c588f',NULL,NULL,NULL,NULL),(8,'Lelianto Eko','lian@alterra.id','a44a8e7d7fc9207dbb026fb1bab51909',NULL,NULL,NULL,NULL),(9,'Lelianto','lelianto.eko@gmail.com','a44a8e7d7fc9207dbb026fb1bab51909',NULL,NULL,NULL,NULL),(10,'Lelianto Pradana','lelianto.pradana@gmail.com','a44a8e7d7fc9207dbb026fb1bab51909',NULL,NULL,NULL,NULL),(11,'Lian Eko','lelianto99@yahoo.co.id','a44a8e7d7fc9207dbb026fb1bab51909',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-20 16:12:13
