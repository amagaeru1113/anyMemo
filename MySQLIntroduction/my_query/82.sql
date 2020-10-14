# 82 演習

/*
メルマガ送信ようのリスト作成
出力項目
	宛名　苗字+さん
    email
条件
	女性だけに送信したい
*/

select 
	concat(last_name , 'さん'),
    email
from 
	users
where
	gender = 2
;