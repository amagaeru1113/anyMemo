# 44 列の値に対して演算を行う
# 商品一覧に税込価格を追加して欲しい

select 
	name as 名前,
    price as 価格,
    price * 1.10 as 税込価格
from
	mydb.products;