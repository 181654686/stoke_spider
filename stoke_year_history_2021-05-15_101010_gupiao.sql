/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS stoke_year_history;
CREATE TABLE `stoke_year_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `years` varchar(45) DEFAULT NULL,
  `cashflow` varchar(45) DEFAULT NULL,
  `debtratio` varchar(45) DEFAULT NULL,
  `grossprofit` varchar(45) DEFAULT NULL,
  `income` varchar(45) DEFAULT NULL,
  `profit` varchar(45) DEFAULT NULL,
  `profit_kf` varchar(45) DEFAULT NULL,
  `roa` varchar(45) DEFAULT NULL,
  `roe` varchar(45) DEFAULT NULL,
  `stoke_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4;