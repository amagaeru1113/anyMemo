# 95 演習

/*
全ての商品について販売個数の一覧を出して

注文詳細についてはorder_detailsにあるalter
販売個数はproduct_qty

*/

select
	p.id,
    p.name,
    sum(o.product_qty) num
from 
	products p
left join -- inner joinだと一個以上販売されているものが表示される
	order_details o
    on p.id = o.product_id
group by
	p.id
;