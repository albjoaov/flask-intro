CREATE TABLE myusers (
  id serial,
  password VARCHAR NOT NULL,
  CHECK (password <> ''),
  email VARCHAR UNIQUE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);
INSERT INTO users(password, email)
VALUES('123', 'email@email.com')

select * from users;

select * from users u WHERE u.id = 13

UPDATE table_name
SET column1 = value1,
    column2 = value2,
    ...
WHERE condition;

UPDATE users
SET password = '987654321'
WHERE id = 1

DELETE FROM users WHERE id = 6


