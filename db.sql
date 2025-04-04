CREATE DATABASE IF NOT EXISTS helixdb;
USE helixdb;

CREATE TABLE user IF NOT EXISTS(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    passwd_sha256 TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE messages (
    sender BIGINT NOT NULL,
    receiver BIGINT NOT NULL,
    message TEXT NOT NULL,
    ts BIGINT NOT NULL,
    PRIMARY KEY (sender)
);
