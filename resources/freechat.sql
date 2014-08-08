DROP DATABASE IF EXISTS freechat;
CREATE DATABASE freechat;
USE freechat;

DROP TABLE IF EXISTS user;
CREATE TABLE user (
	uid bigint(20) AUTO_INCREMENT,
	name varchar(32),
	password varchar(32) NOT NULL,
	gender int(1) NOT NULL DEFAULT 0,
	avatar varchar(64),
	status int(1) NOT NULL DEFAULT 0,
	emotion varchar(128),
	token varchar(64),
	create_time bigint(20) NOT NULL DEFAULT 0,
	update_time bigint(20),
	is_active int(1) NOT NULL DEFAULT 1, 
	is_deleted int(1) NOT NULL DEFAULT 0,
	PRIMARY KEY(uid)
)ENGINE = InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS friendship;
CREATE TABLE friendship (
	uid bigint(20) NOT NULL,
	friend_id bigint(20) NOT NULL,
	alias_name varchar(32),
	is_deleted int(1) NOT NULL DEFAULT 0,
	create_time bigint(20) NOT NULL DEFAULT 0,
	update_time bigint(20),
	PRIMARY KEY (uid, friend_id)
)ENGINE = InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS message;
CREATE TABLE message (
	id bigint(20) AUTO_INCREMENT,
	sender bigint(20) NOT NULL,
	receiver bigint(20) NOT NULL,
	type int(1) NOT NULL,
	content text NOT NULL,
	send_time bigint(20) NOT NULL,
	receive_time bigint(20) NOT NULL DEFAULT 0,
	PRIMARY KEY(id)
)ENGINE = InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE message ADD INDEX message_receiver_idx(receiver, receive_time);
ALTER TABLE message ADD INDEX message_sender_receiver_idx(sender, receiver, receive_time);

