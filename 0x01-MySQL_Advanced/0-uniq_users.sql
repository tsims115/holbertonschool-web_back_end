--- creates table of user with id, email, name
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(250) unique NOT NULL,
    name varchar(250),
    PRIMARY KEY (id)
);
