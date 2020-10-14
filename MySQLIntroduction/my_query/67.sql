# 67 集約結果をさらに絞り込むhaving

 # 2017年のアクセスログから、月間ユニークユーザー数が630人以上の月を一覧にして
 
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
having -- group by の後に記述する
	count(distinct user_id) >= 630
;