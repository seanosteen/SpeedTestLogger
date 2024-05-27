CREATE TABLE `SpeedTestResults` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `timeStamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `ping_latency` decimal(10,2) NOT NULL,
  `download_bandwidth` decimal(10,2) NOT NULL,
  `download_jitter` decimal(10,2) NOT NULL,
  `upload_bandwidth` decimal(10,2) NOT NULL,
  `upload_jitter` decimal(10,2) NOT NULL,
  `packetLoss` decimal(4,2) NOT NULL,
  `externalIP` varchar(30) NOT NULL,
  `server_location` varchar(60) NOT NULL,
  `server_ip` varchar(50) DEFAULT NULL,
  `server_sponsor` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_timestamp` (`timeStamp`)
) COMMENT='Primary logging table';


CREATE TABLE `Errors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `logDate` datetime NOT NULL DEFAULT current_timestamp(),
  `errorText` text NOT NULL,
  PRIMARY KEY (`id`)
) COMMENT='Error Message and Stack Traces for Failed Runs';