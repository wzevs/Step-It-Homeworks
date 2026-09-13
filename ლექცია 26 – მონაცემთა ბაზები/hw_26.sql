CREATE DATABASE IF NOT EXISTS hw_26;
USE hw_26;

CREATE TABLE Authors (
    AuthorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL
);

CREATE TABLE Books (
    BookID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    PublishYear INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

-- ავტორების დამატება
INSERT INTO Authors (FirstName, LastName) VALUES 
('ილია', 'ჭავჭავაძე'),
('აკაკი', 'წერეთელი'),
('ვაჟა', '-ფშაველა'),
('გალაქტიონ', 'ტაბიძე'),
('მიხეილ', 'ჯავახიშვილი');

-- წიგნების დამატება (AuthorID ემთხვევა ზემოთ შექმნილ ავტორებს)
INSERT INTO Books (Title, PublishYear, AuthorID) VALUES 
('კაცია-ადამიანი?!', 1863, 1),
('ბაში-აჩუკი', 1889, 2),
('ალუდა ქეთელაური', 1888, 3),
('მერი', 1915, 4),
('ჯაყოს ხიზნები', 1925, 5);

-- ვაახლებთ პირველი წიგნის გამოცემის წელს
UPDATE Books 
SET PublishYear = 1864 
WHERE BookID = 1;

SELECT 
    Books.Title AS 'წიგნის სათაური', 
    Books.PublishYear AS 'გამოცემის წელი', 
    Authors.FirstName AS 'ავტორის სახელი', 
    Authors.LastName AS 'ავტორის გვარი'
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID;


DELETE FROM Books;
DELETE FROM Authors;

DROP TABLE Books;
DROP TABLE Authors;