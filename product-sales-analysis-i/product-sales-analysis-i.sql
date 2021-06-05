# Write your MySQL query statement below
# select 
#         p.product_name,
#         s.year,
#         s.price
# from 
#         Product p
# join 
#         Sales s
# on      
#         s.product_id = p.product_id
select 
        p.product_name,
        s.year,
        s.price
from 
        Product p
join 
        (select 
                Distinct 
                        product_id,
                        year,
                        price 
                from Sales 
        ) as s
using (product_id);

    
        