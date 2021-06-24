# Write your MySQL query statement below
select Distinct l1.Num as ConsecutiveNums
from Logs l1,Logs l2,Logs l3
where l1.id+1 = l2.id and l2.id+1=l3.id and l1.Num = l2.Num and l2.Num=l3.Num