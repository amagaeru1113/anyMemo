# 130 削除条件にサブクエリを使う

# 一個も売れていない商品を削除して


select
	product_id
from 
	order_details
group by
	product_id
;

delete from products
where
	id not in 
    (
    select
		product_id
	from 
		order_details
	group by
		product_id
    )
;