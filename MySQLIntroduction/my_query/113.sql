# 113 演習

/*
全商品を累計販売個数でランクわけして欲しい
*/


select 
	p.id product_id,
    p.name product_name,
    sum(od.product_qty) num,
    case
        when sum(od.product_qty) >= 20 then 'A'
        when sum(od.product_qty) >= 10 then 'B'
        else 'C'
    end as product_rank

from
	products p
left join
	order_details od
	on p.id = od.product_id
group by
	p.id
order by
	product_rank asc
;

