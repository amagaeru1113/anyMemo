# 69 演習

# 全てのアクセスログ一覧を出して
select
	*
from 
	access_logs
;

# 出力は2017年1月〜6月までにして
select
	*
from 
	access_logs
where
	request_month >= '2017-01-01' 
    and request_month < '2017-07-01'
;

# 出力した月ごとのリクエスト数を教えて
select
	request_month,
	count(*)
from 
	access_logs
where
	request_month >= '2017-01-01' 
    and request_month < '2017-07-01'
group by
	request_month
	
;

# 出力した月でアクセス数が1000以上の月だけを抜き出した
select
	request_month,
	count(*)
from 
	access_logs
where
	request_month >= '2017-01-01' 
    and request_month < '2017-07-01'
group by
	request_month
having
	count(*) >= 1000
;

