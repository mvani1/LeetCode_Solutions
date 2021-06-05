# Write your MySQL query statement below
select
        Distinct player_id,
        min(event_date) as first_login
from 
        Activity
group by player_id;
