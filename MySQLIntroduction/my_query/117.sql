# 117 月別平均客単価

select
	date_format(order_time, '%Y%m') order_y_m,
    round(avg(amount),0) average_customer_spend
from 
	orders o
group by
	date_format(order_time, '%Y%m')
order by
	order_y_m asc
;