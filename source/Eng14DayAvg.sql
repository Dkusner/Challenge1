select e1.createdAt, e1.type, avg(e2.count) 14DayAvg
from test.engagements e1
join 
(select createdAt, type, count(*) count
from test.engagements
group by 1,2)
as e2
on e1.type = e2.type
and datediff(e1.createdAt, e2.createdAt) BETWEEN 0 AND 13
group by 1,2;