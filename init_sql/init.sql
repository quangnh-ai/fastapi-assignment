CREATE TABLE IF NOT EXISTS user_table (
    id serial NOT NULL,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    hashed_password TEXT NOT NULL,
    is_active BOOLEAN,
    is_superuser BOOLEAN,
    PRIMARY KEY (id)
);

INSERT INTO user_table (
    email, 
    first_name, 
    last_name, 
    hashed_password, 
    is_active, 
    is_superuser
)
VALUES(
    'admin@admin.com',
    'Admin',
    'Admin',
    '$2b$12$oEGUgQRj7X1RyWb7ANQqtu1BO6vsv7tLTLqBRiexEliiJXKMGWjwm',
    '1',
    '1'
);

CREATE TABLE IF NOT EXISTS book (
    id serial NOT NULL,
    title TEXT,
    author TEXT,
    publish_date DATE,
    isbn TEXT NOT NULL,
    price FLOAT,
    PRIMARY KEY (id)
);

INSERT INTO book (
    title, 
    author, 
    publish_date, 
    isbn, 
    price
)
VALUES(
    'IT Book',
    'IT Man',
    '2023-01-01',
    '111111111',
    9.99
),
(
    'Cook Book',
    'Chef',
    '2023-02-01',
    '222222222',
    10.99
),
(
    'Electronic Book',
    'Engineer',
    '2023-03-01',
    '333333333',
    4.99
);