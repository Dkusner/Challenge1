select createdAt, type, count(*) type_daily_count
from test.engagements
group by createdAt, type;