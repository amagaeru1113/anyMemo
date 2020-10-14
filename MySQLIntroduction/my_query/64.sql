# 64 ユニークユーザー数を求める

# 2017年1月にアクセスした、ユニークユーザー数（ECサイト登録者のみ）を教えて
# ここでのユニークユーザー：決まった集計期間内にアクセスしたユーザーの数を表す数値
# アクセス情報はaccess_log

use mydb;

select 
	count(distinct user_id) 
from 
	access_logs
where 
	request_month = '2017-01-01'
;