-- Write your PostgreSQL query statement below
SELECT product_name, unit FROM (SELECT product_id, sum(o.unit) as unit FROM Orders o
WHERE o.order_date BETWEEN 2020-02-01 AND 2020-02-29 
GROUP BY product_id) ord JOIN Products prod ON ord.product_id = prod.product_id WHERE ord.unit >= 100;
