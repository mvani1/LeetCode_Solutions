# Write your MySQL query statement below
select score,dense_rank() over(order by Score Desc)'Rank'
from Scores