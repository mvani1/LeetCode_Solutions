# Write your MySQL query statement belows

select
        distinct c.title
from
        (select content_id , title from Content where content_type = 'Movies' and kids_content = 'Y') c
join TVProgram p
on p.content_id = c.content_id
where p.program_date between '2020-06-01' and '2020-06-30'
