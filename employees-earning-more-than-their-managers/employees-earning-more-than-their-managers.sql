# Write your MySQL query statement below
select e.Name as 'Employee'
from Employee e, Employee e2
where e.ManagerId = e2.id and e.salary>e2.salary