--- creaetes table of user with id, email, name
CREATE TABLE users (
    id int NOT NULL AUTOINCREMENT PRIMARY KEY,
    email varchar(250),
    name varchar(250)
) IF NOT EXISTS;
