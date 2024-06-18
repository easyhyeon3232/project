# DDL(CREATE, ALTER, DROP) 테이블을 정의하는 SQL

CREATE TABLE `newuser (
	`name` VARCHAR(10) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`email` VARCHAR(20) NOT NULL COLLATE 'utf8mb4_general_ci',
	`password_hash` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`birthdate` DATE NULL DEFAULT NULL,
	PRIMARY KEY (`email`) USING BTREE
)
COMMENT='회원가입'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1
;