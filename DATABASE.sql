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
  `id` varchar(50) NOT NULL DEFAULT '',
  `exp` int(50) NOT NULL DEFAULT 0,
  `level` int(11) NOT NULL DEFAULT 1,
  `date` varchar(100) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 테이블 데이터 irobot.chat_player:~14 rows (대략적) 내보내기
/*!40000 ALTER TABLE `chat_player` DISABLE KEYS */;
INSERT INTO `chat_player` (`id`, `exp`, `level`, `date`) VALUES
	('169678500893163520', 20, 1, '0'),
	('172002275412279296', 0, 1, '0'),
	('184405311681986560', 15, 1, '0'),
	('185476724627210241', 15, 1, '0'),
	('252025791007817728', 35, 1, '0'),
	('277080328269594625', 40, 1, '1585119357'),
	('305630277852594176', 0, 1, '0'),
	('324196735985647627', 610, 6, '1585119240'),
	('351427090123587587', 115, 2, '1585119938'),
	('378562158260256789', 100, 2, '1585110720'),
	('384064343714693122', 25, 1, '0'),
	('389267978425860096', 300, 4, '0'),
	('399828403659997214', 95, 2, '1585119946'),
	('418995840338755584', 45, 1, '1585111217'),
	('423843986122342401', 0, 1, '1585125783');
/*!40000 ALTER TABLE `chat_player` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
