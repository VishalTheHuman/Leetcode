# Write your MySQL query statement below
SELECT MAX(T.num) as num FROM (SELECT num FROM MyNumbers GROUP BY num HAVING COUNT(num)=1) AS T;
