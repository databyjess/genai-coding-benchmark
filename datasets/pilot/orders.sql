CREATE TABLE orders (
order_id INT,
user_id INT,
amount NUMERIC,
placed_at TIMESTAMP
);


INSERT INTO orders VALUES
(1, 1, 100, '2024-01-05'),
(2, 1, 50, '2024-02-01'),
(3, 2, 75, '2024-03-01'),
(4, 3, 200, '2024-02-15');