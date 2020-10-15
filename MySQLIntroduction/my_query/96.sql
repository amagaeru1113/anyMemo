# 96 三つ以上のテーブルを使った結合

/*
注文一覧を出して欲しい
注文詳細と商品情報も一覧の中に入れて欲しい

追加
user_idだと誰かわからないので、名字と名前を出して欲しい
*/

select 
	o.id order_id,
    o.user_id user_id,
    u.last_name last_name,
    u.first_name first_name,
    o.amount amount,
    o.order_time order_time,
    p.name product_name,
    od.product_qty qty
from
 	orders o
inner join
	order_details od
	on o.id = od.order_id
inner join
	products p
    on od.product_id = p.id
inner join
	users u
    on o.user_id = u.id
;
