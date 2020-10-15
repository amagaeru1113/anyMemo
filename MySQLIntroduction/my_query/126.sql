# 126 更新条件にサブクエリを使う

# 累計販売数が10を超えている商品については価格を5%upして

select 
	product_id, 
    sum(product_qty) 
from 
	order_details 
group by 
	product_id
having
	sum(product_qty) >= 10
;


update 
	products
set
	price = price * 1.05
where
	id in 
	(
    select 
		product_id
	from 
		order_details 
	group by 
		product_id
	having
		sum(product_qty) >= 10
    )
;

