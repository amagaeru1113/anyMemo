# データをグループ化

# 都道府県べつのユーザー数を教えて
# prefecture_idのみでおk
# 結合してみて都道府県名が分かるようにした

use mydb;

select
	prefectures.name,
    count(*)
from 
	users
INNER JOIN 
	prefectures ON users.prefecture_id = prefectures.id
group by
	prefectures.name
;