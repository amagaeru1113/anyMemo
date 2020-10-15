# 90 内部結合+絞り込み


/*
顧客一覧を取得して
都道府県iDで出力せず、都道府県名を表示して
必要な列はユーザーiD、苗字、名前、都道府県めい

追加条件
女性だけのデータが欲しい
*/
use mydb;



select 
	u.id ユーザーID,
    u.last_name 名字,
    u.first_name 名前,
    p.name 都道府県名
from 
	users u
inner join 
	prefectures p 
    on u.prefecture_id = p.id
where
	u.gender = 2
;
