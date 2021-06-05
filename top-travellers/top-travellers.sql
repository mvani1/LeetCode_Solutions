# Write your MySQL query statement below
select
        name,
        sum(ifnull(r.distance,0)) as travelled_distance
from 
        Users u
        left join rides r
        on r.user_id = u.id
group by u.name
order by travelled_distance DESC,name;