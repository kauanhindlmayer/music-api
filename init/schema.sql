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