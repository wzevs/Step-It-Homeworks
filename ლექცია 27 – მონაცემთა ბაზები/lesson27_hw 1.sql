-- 1. მონაცემთა ბაზის შექმნა
CREATE DATABASE IF NOT EXISTS lesson27_hw;
USE lesson27_hw;

-- 2. ძველი ცხრილების წაშლა (თუ უკვე არსებობს), რათა თავიდან ავიცილოთ დუბლიკატები
DROP TABLE IF EXISTS migrations;
DROP TABLE IF EXISTS sea_lions;

-- 3. ცხრილების შექმნა
CREATE TABLE sea_lions (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    species VARCHAR(50)
);

CREATE TABLE migrations (
    id INT,
    distance INT,
    days INT
);

-- 4. მონაცემების ჩასმა sea_lions ცხრილში
INSERT INTO sea_lions (id, name, species) VALUES
(10484, 'Ayah', 'Zalophus californianus'),
(11728, 'Spot', 'Zalophus californianus'),
(11729, 'Tiger', 'Zalophus californianus'),
(11732, 'Mabel', 'Zalophus californianus'),
(11734, 'Rick', 'Zalophus californianus'),
(11790, 'Jolee', 'Zalophus californianus');

-- 5. მონაცემების ჩასმა migrations ცხრილში
INSERT INTO migrations (id, distance, days) VALUES
(10484, 1000, 107),
(11728, 1531, 56),
(11729, 1370, 37),
(11732, 1622, 62),
(11734, 1491, 58),
(11735, 2723, 82),
(11736, 1571, 52),
(11737, 1957, 92);

-- 6. JOIN ოპერაციები
-- INNER JOIN
SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations m
JOIN sea_lions s ON m.id = s.id;

-- LEFT JOIN
SELECT m.id, m.distance, m.days, s.name, s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id;

-- RIGHT JOIN
SELECT s.id, s.name, s.species, m.distance, m.days
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;

-- FULL JOIN ემულაცია UNION-ით (დუბლიკატების გარეშე)
SELECT m.id AS mig_id, m.distance, m.days, s.id AS lion_id, s.name, s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
UNION
SELECT m.id, m.distance, m.days, s.id, s.name, s.species
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;

-- FULL JOIN ემულაცია UNION ALL-ით (დუბლიკატებით)
SELECT m.id AS mig_id, m.distance, m.days, s.id AS lion_id, s.name, s.species
FROM migrations m
LEFT JOIN sea_lions s ON m.id = s.id
UNION ALL
SELECT m.id, m.distance, m.days, s.id, s.name, s.species
FROM migrations m
RIGHT JOIN sea_lions s ON m.id = s.id;