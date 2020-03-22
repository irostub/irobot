-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.4.11-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- irobot 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `irobot` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `irobot`;

-- 테이블 irobot.chat_player 구조 내보내기
CREATE TABLE IF NOT EXISTS `chat_player` (
  `id` char(100) NOT NULL,
  `exp` int(50) NOT NULL DEFAULT 0,
  `level` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 테이블 데이터 irobot.chat_player:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `chat_player` DISABLE KEYS */;
INSERT INTO `chat_player` (`id`, `exp`, `level`) VALUES
	('252025791007817728', 5, 1),
	('351427090123587587', 60, 2);
/*!40000 ALTER TABLE `chat_player` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
