# Write your MySQL query statement below
# select ue.unique_id, e.name
# from Employees as e
# left join EmployeeUNI as ue
# on e.id = ue.id;

select (select unique_id from EmployeeUNI as u where u.id = e.id) as unique_id,
name from 
Employees as e;
