/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS stoke_day_history;
CREATE TABLE `stoke_day_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(45) DEFAULT NULL,
  `guxi` varchar(45) DEFAULT NULL,
  `pea` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `value` varchar(45) DEFAULT NULL,
  `pb` varchar(45) DEFAULT NULL,
  `stoke_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;