CREATE DATABASE IF NOT EXISTS music_api_database;

CREATE TABLE IF NOT EXISTS `music_api_database`.`genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(45) NOT NULL,
  `created_at` timestamp NOT NULL,
  `modified_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE IF NOT EXISTS `music_api_database`.`musics` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `duration` timestamp NOT NULL,
  `genre_id` int DEFAULT NULL,
  `release_date` timestamp NOT NULL,
  `created_at` timestamp NOT NULL,
  `modified_at` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `musics_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`)
)

CREATE TABLE IF NOT EXISTS `music_api_database`.`record_label` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `contract_value` int NOT NULL,
  `expire_date` timestamp NOT NULL,
  `created_at` timestamp NOT NULL,
  `modified_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
)

CREATE TABLE IF NOT EXISTS `music_api_database`.`subscriptions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `description` varchar(45) NOT NULL,
  `value` decimal(5,2) NOT NULL,
  `limit` int NOT NULL,
  `created_at` timestamp NOT NULL,
  `modified_at` timestamp NOT NULL,
  PRIMARY KEY (`id`)
)

-- Ensure that the genre_id column references an existing id in the genres table
DELIMITER //

CREATE TRIGGER musics_genre_id_trigger
BEFORE INSERT ON `music_api_database`.`musics`
FOR EACH ROW
BEGIN
  IF NEW.genre_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM `music_api_database`.`genres` WHERE id = NEW.genre_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Foreign key constraint violation: Invalid genre_id.';
  END IF;
END//

DELIMITER ;

-- Ensure that the release_date is not in the future
DELIMITER //

CREATE TRIGGER musics_release_date_trigger
BEFORE INSERT ON `music_api_database`.`musics`
FOR EACH ROW
BEGIN
  IF NEW.release_date > NOW() THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Release date cannot be in the future.';
  END IF;
END//

DELIMITER ;

-- Ensure that the expire_date is greater than the created_at
DELIMITER //

CREATE TRIGGER record_label_expire_date_trigger
BEFORE INSERT ON `music_api_database`.`record_label`
FOR EACH ROW
BEGIN
  IF NEW.expire_date <= NEW.created_at THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Expire date must be greater than created_at.';
  END IF;
END//

DELIMITER ;

-- Ensure that the value is greater than 0
DELIMITER //

CREATE TRIGGER subscriptions_value_trigger
BEFORE INSERT ON `music_api_database`.`subscriptions`
FOR EACH ROW
BEGIN
  IF NEW.value <= 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Value must be greater than 0.';
  END IF;
END//

DELIMITER ;