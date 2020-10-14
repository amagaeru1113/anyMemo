# 106 演習

# 105 サブクエリ（where句）

/*
2017年12月に商品を購入したユーザーにメルマガを出したいので
該当ユーザー一覧を出して欲しい

出力は ユーザーid、苗字、email
*/

select 
	id,
    last_name,
    email
from 
	users	
where
	id in (
		select 
			user_id 
		from 
			orders 
		where 
			order_time >= '2017-12-01 00:00:00' and order_time < '2018-01-01 00:00:00'
    )
;

