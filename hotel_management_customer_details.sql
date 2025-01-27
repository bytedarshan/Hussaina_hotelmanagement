-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel_management
-- ------------------------------------------------------
-- Server version	5.7.43-log

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
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_details` (
  `C_ID` int(4) NOT NULL,
  `C_name` varchar(20) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `C_email` varchar(20) DEFAULT NULL,
  `C_phone_no` varchar(10) DEFAULT NULL,
  `C_aadhar` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT INTO `customer_details` VALUES (1236,'MRS SHIRLEY HUMMER','SRI LANKA','shirley@gmail.com','8150462845','487032759467'),(1872,'werty','wertyu','werty','345','3456789'),(2480,'husaina','india','gmail@gmail.com','456456','345678'),(3163,'husaina','india','hu@gmail.com','214759432','23456789'),(4454,'wert','wert','wertyu','234567','2345678'),(4561,'MR JACK FINNEY','AUSTRIA','jack@gmail.com','9452305841','287046167356'),(4588,'MR AUGUSTUS WATERS','SPAIN','augustus@gmail.com','8603458216','205683418460'),(6648,'dfghj','dfgh','wertyui','3456','2345678'),(6664,'ert','ertyu','ertyu','3456','23456789'),(7882,'erty','ertyu','ertyu','2345678','34567890'),(7894,'MRS LATA SHARMA','INDIA','lata@gmail.com','8720673416','698230671258'),(8194,'husaina','india','h@gmail.com','1234678','12345678'),(8786,'MR B.B.ROY','INDIA','bbroy@gmail.com','8793654508','354792766545'),(8935,'erty','rtyui','tyuio','234','123456'),(9769,'ertyu','ertyu','dfghjk','34567','23456789');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-05  9:20:47
