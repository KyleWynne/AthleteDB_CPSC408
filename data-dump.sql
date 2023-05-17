-- MySQL dump 10.13  Distrib 8.0.32, for macos12.6 (x86_64)
--
-- Host: localhost    Database: Athlete
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `allplayers`
--

DROP TABLE IF EXISTS `allplayers`;
/*!50001 DROP VIEW IF EXISTS `allplayers`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `allplayers` AS SELECT 
 1 AS `TID`,
 1 AS `player_name`,
 1 AS `salary`,
 1 AS `age`,
 1 AS `sport`,
 1 AS `trophies`,
 1 AS `teamID`,
 1 AS `team_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `gameID` int NOT NULL AUTO_INCREMENT,
  `team1ID` int DEFAULT NULL,
  `team2ID` int DEFAULT NULL,
  `team1_score` int NOT NULL,
  `team2_score` int NOT NULL,
  `outcome` varchar(30) NOT NULL,
  PRIMARY KEY (`gameID`),
  KEY `team1ID` (`team1ID`),
  KEY `team2ID` (`team2ID`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`team1ID`) REFERENCES `teams` (`teamID`),
  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`team2ID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (2,4,3,105,121,'Win'),(3,12,9,3,2,'Win'),(4,13,2,2,4,'Loss'),(5,7,6,121,101,'Win'),(6,7,6,1105,130,'Win'),(7,3,4,130,100,'Win'),(8,14,16,28,21,'Win'),(9,14,15,21,35,'Loss');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `leagues`
--

DROP TABLE IF EXISTS `leagues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leagues` (
  `leagueID` int NOT NULL AUTO_INCREMENT,
  `league_name` varchar(30) NOT NULL,
  `sport` varchar(30) NOT NULL,
  `country` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`leagueID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `leagues`
--

LOCK TABLES `leagues` WRITE;
/*!40000 ALTER TABLE `leagues` DISABLE KEYS */;
INSERT INTO `leagues` VALUES (1,'NULL','NULL','NULL'),(5,'NHL','Hockey','America'),(8,'MLB','Baseball','America'),(11,'NFL','Football','America'),(13,'Premier League','Soccer','England'),(14,'NBA','Basketball','America');
/*!40000 ALTER TABLE `leagues` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `playerID` int NOT NULL AUTO_INCREMENT,
  `player_name` varchar(30) NOT NULL,
  `salary` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sport` varchar(30) NOT NULL,
  `trophies` int DEFAULT NULL,
  `teamID` int DEFAULT NULL,
  PRIMARY KEY (`playerID`),
  KEY `teamID` (`teamID`),
  KEY `player_index` (`playerID`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`teamID`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'NULL',0,0,'NULL',0,1),(4,'Joel Embiid',36320000,29,'Baseball',2,3),(5,'James Harden',34320000,33,'Basketball',1,3),(6,'Tiger Woods',68000000,47,'Golf',5,1),(9,'Jason Tatum',30000000,31,'BasketBall',1,4),(12,'Anthony Davis',37980000,30,'BasketBall',0,7),(13,'Steph Curry',37980000,35,'BasketBall',2,6),(14,'Lionel Messi',35000000,35,'Soccer',7,9),(15,'Kylian Mbappe',72000000,24,'Soccer',1,9),(16,'Erling Haaland',26017124,22,'Soccer',0,10),(17,'Virgil Van Dijk',21000000,31,'Soccer',3,10),(18,'Nathan Mackinnon',6850000,27,'Hockey',2,2),(19,'Joe Thorton',5000000,27,'Hockey',2,13),(20,'Aaron Rodgers',22000000,27,'Football',4,16),(21,'Tom Brady',37500000,45,'Football',3,15),(22,'Brock Purdy',934252,23,'Football',0,14);
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `teamID` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(30) NOT NULL,
  `leagueID` int NOT NULL,
  `trophies` int DEFAULT NULL,
  PRIMARY KEY (`teamID`),
  KEY `team_index` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (1,'NULL',1,0),(2,'Colarado Avalanche',5,1),(3,'76ers',14,3),(4,'Celtics',14,17),(6,'Warriors',14,6),(7,'Lakers',14,17),(8,'Heat',14,3),(9,'PSG',13,11),(10,'Manchester City',13,1),(12,'Liverpool',13,19),(13,'San Jose Sharks',5,0),(14,'49ers',11,5),(15,'Patriots',11,6),(16,'Packers',11,4);
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trophies`
--

DROP TABLE IF EXISTS `trophies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trophies` (
  `trophyID` int NOT NULL AUTO_INCREMENT,
  `trophy_name` varchar(30) NOT NULL,
  `leagueID` int NOT NULL,
  `year` year DEFAULT NULL,
  `player_winner_id` int DEFAULT NULL,
  `team_winner_id` int DEFAULT NULL,
  PRIMARY KEY (`trophyID`),
  KEY `leagueID` (`leagueID`),
  KEY `player_winner_id` (`player_winner_id`),
  KEY `team_winner_id` (`team_winner_id`),
  CONSTRAINT `trophies_ibfk_1` FOREIGN KEY (`leagueID`) REFERENCES `leagues` (`leagueID`),
  CONSTRAINT `trophies_ibfk_2` FOREIGN KEY (`player_winner_id`) REFERENCES `players` (`playerID`),
  CONSTRAINT `trophies_ibfk_3` FOREIGN KEY (`team_winner_id`) REFERENCES `teams` (`teamID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trophies`
--

LOCK TABLES `trophies` WRITE;
/*!40000 ALTER TABLE `trophies` DISABLE KEYS */;
INSERT INTO `trophies` VALUES (1,'MVP',14,2023,4,1),(9,'Stanley Cup',5,2022,1,2),(12,'DPOY',14,2023,9,1),(13,'MVP',11,2020,20,1),(14,'MVP',11,2021,20,1),(15,'Super Bowl',11,2019,1,15),(16,'Super Bowl',11,2017,1,15),(17,'Super Bowl',11,2015,1,15),(18,'Super Bowl',11,2005,1,15),(19,'Super Bowl',11,2004,1,15),(20,'Super Bowl',11,2002,1,15),(21,'NBA Championship',14,2022,1,6),(22,'Ballon dOr',13,2012,14,1),(23,'Ballon dOr',13,2013,14,1),(24,'Ballon dOr',13,2016,14,1),(25,'Ballon dOr',13,2019,14,1),(26,'Ballon dOr',13,2021,14,1),(27,'Premier League Championship',13,2022,1,9),(28,'Premier League Championship',13,2019,1,12);
/*!40000 ALTER TABLE `trophies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `allplayers`
--

/*!50001 DROP VIEW IF EXISTS `allplayers`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `allplayers` AS select `players`.`teamID` AS `TID`,`players`.`player_name` AS `player_name`,`players`.`salary` AS `salary`,`players`.`age` AS `age`,`players`.`sport` AS `sport`,`players`.`trophies` AS `trophies`,`teams`.`teamID` AS `teamID`,`teams`.`team_name` AS `team_name` from (`players` join `teams` on((`players`.`teamID` = `teams`.`teamID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-17 12:17:16
