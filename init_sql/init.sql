CREATE TABLE IF NOT EXISTS users (
    id serial NOT NULL,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN,
    is_superuser BOOLEAN,
    is_authenticated BOOLEAN,
    PRIMARY KEY (id)
);

INSERT INTO users (
    email, 
    first_name, 
    last_name, 
    hashed_password, 
    is_active, 
    is_superuser,
    is_authenticated
)
VALUES(
    'admin@admin.com',
    'Admin',
    'Admin',
    '$2b$12$oEGUgQRj7X1RyWb7ANQqtu1BO6vsv7tLTLqBRiexEliiJXKMGWjwm',
    '1',
    '1',
    '1'
),
(
    'test@test.com',
    'Test',
    'Test',
    '$2b$12$AmQ/3Z9Vp32BFjdjZvww2OJ5WN0TPmaFAy2JIlOtGe4Pu/gWDMqLW',
    '1',
    '1',
    '0'
),
(
    'quang@quang.com',
    'Quang',
    'Nguyen',
    '$2b$12$047UnWdSjcZZL/q4in.fKOV/0XYtAQNa2oY9L5yKW570eK7itMQaa',
    '1',
    '0',
    '1'
),
(
    'another@another.com',
    'Another',
    'Another',
    '$2b$12$a7VE0Yd3VU/uZV5G5EZ0tOwJoSGlhGtuHsl2EQvXdHzC4oLbyT1KK',
    '1',
    '0',
    '0'
);

CREATE TABLE IF NOT EXISTS books (
    id serial NOT NULL,
    title TEXT,
    author TEXT,
    publish_date DATE,
    isbn TEXT NOT NULL,
    image_link TEXT,
    price FLOAT,
    PRIMARY KEY (id)
);

INSERT INTO books (
    title, 
    author, 
    publish_date, 
    isbn,
    image_link,
    price
)
VALUES(
    'IT Book',
    'IT Man',
    '2023-01-01',
    '111111111',
    'http://localhost:8081/api/v1/books/show_image/?path=/images/111111111.jpg',
    9.99
),
(
    'Cook Book',
    'Chef',
    '2023-02-01',
    '222222222',
    'http://localhost:8081/api/v1/books/show_image/?path=/images/222222222.jpg',
    10.99
),
(
    'Electricity Book',
    'Engineer',
    '2023-03-01',
    '333333333',
    'http://localhost:8081/api/v1/books/show_image/?path=/images/333333333.jpg',
    4.99
);