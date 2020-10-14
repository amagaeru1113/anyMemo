# 58 合計値を求めるsum集約関数
# 2017年1月の合計売上を算出

# 注文情報はordersにある
use mydb;

select 
	sum(amount)
from  
	orders
where
-- 	order_time >= '2017-01-01 00:00:00' and order_time < '2017-02-01 00:00:00'
	order_time between '2017-01-01 00:00:00' and '2017-02-01 00:00:00'
;