# 66 期間ごとに集計する

# 2017年の月別ユニークユーザー数を教えて

select
	request_month,
    count(distinct user_id)
from 
	access_logs
where
	request_month >= '2017-01-01'
    and request_month < '2018-01-01'
group by	
	request_month
;