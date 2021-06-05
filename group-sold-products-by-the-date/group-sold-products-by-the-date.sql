# Write your MySQL query statement below
select 
        sell_date,
        Count(Distinct(product))  as num_sold,
        GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
from 
    activities
group by sell_date