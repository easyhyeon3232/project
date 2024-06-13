# DDL(CREATE, ALTER, DROP) 테이블을 정의하는 SQL

CREATE TABLE `test` (
	`no` INT(10) NOT NULL AUTO_INCREMENT,
	`title` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	`review` VARCHAR(500) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`score` INT(10) NOT NULL DEFAULT '0',
	`writer` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`reg_date` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`no`) USING BTREE
)
COMMENT='다음 영화 리뷰'
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=1
;