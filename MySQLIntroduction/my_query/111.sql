# 111 取得ちnullを0に置き換える

select
	p.id,
    p.name,
    case
		when sum(od.product_qty) is null then 0
        else sum(od.product_qty)
    end as num
from
	products p
left join
	order_details od
	on p.id = od.product_id
group by
	p.id
;