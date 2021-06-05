# Write your MySQL query statement below
select
        s.student_id,
        s.student_name,
        e.subject_name,
        count(ee.subject_name) as attended_exams
from 
        Students s
join
        Subjects e
left join
        Examinations as ee
on
        s.student_id = ee.student_id and e.subject_name = ee.subject_name
group by s.student_id ,e.subject_name
order by student_id , subject_name;
