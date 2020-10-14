# 107 演習

# 全商品の平均単価よりも、単価が高い商品の一覧を出力

select
	name,
    price
from
	products
where
	price > (
		select
			avg(price)
		from 
			products
		)
order by
	price desc,
    id asc
;
