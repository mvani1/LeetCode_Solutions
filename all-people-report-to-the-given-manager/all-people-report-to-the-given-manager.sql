# Write your MySQL query statement below
select e1.employee_id
from Employees e1,Employees e2,Employees e3
where e1.manager_id = e2.employee_id
and e2.manager_id = e3.employee_id
and e3.manager_id = '1'
and e1.employee_id !='1'