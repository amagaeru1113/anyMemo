# 92 演習 と回答

/*
2017年1月の東京都に住むユーザーの注文情報一覧を出して
東京都 id = 13

取得する列は
注文id
注文日時
注文金額合計
ユーザーid
名字
名前
*/

select
    o.id 注文ID,
    o.order_time 注文日時,
    o.amount 注文金額合計,
    u.id ユーザーID,
    u.last_name 名字,
    u.first_name 名前
from 
	orders as o
inner join
	users as u
    on o.user_id = u.id
where
	u.prefecture_id = 13
	and
    (o.order_time >= '2017-01-01 00:00:00' and o.order_time < '2017-02-01 00:00:00')
order by
	o.id asc
;

