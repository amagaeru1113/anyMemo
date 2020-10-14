# 59 平均値を求める
# 自社ECサイトで取り扱っている全商品の平均価格を教えて

# 商品情報はproducts

select
	avg(price)
from
	mydb.products
;