CREATE DATABASE library;
USE library;

CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    `year` INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO books (id, title, author, `year`, price) VALUES
(1, 'The Alchemist', 'Paulo Coelho', 1988, 450.00),
(2, 'Atomic Habits', 'James Clear', 2018, 650.00),
(3, '1984', 'George Orwell', 1949, 520.00),
(4, 'To Kill a Mockingbird', 'Harper Lee', 1960, 480.00),
(5, 'The Hobbit', 'J.R.R. Tolkien', 1937, 700.00),
(6, 'Pride and Prejudice', 'Jane Austen', 1813, 390.00),
(7, 'Clean Code', 'Robert C. Martin', 2008, 850.00),
(8, 'The Little Prince', 'Antoine de Saint-Exupery', 1943, 300.00);

SELECT * FROM books
WHERE price > 500;

SELECT * FROM books
ORDER BY price DESC;

SELECT COUNT(*) AS total_books
FROM books;

UPDATE books
SET price = 475.00
WHERE id = 1;
