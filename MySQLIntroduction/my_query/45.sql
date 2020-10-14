# 45 条件を指定してデータ抽出する
# 商品一覧　必要なのは名前と価格、かつ9800円以上に絞る

select
	name 名前,
    price 価格
from 
	mydb.products
where
	price >= 9800
;