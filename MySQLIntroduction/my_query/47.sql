# 47 パターンマッチングによる絞り込み

/*
ワイルドカード
	%  :  0文字以上の任意の文字列
    _  :  任意の1文字
    
例
	'中%' : 中で始まる文字列
    '%中%': 中を含む文字列
    `%子` : 子で終わる文字列
    '__子': 任意の2文字で始まり、子で終わる文字列
*/

# 漢字の'中'から始まる苗字のユーザー一覧を取得して欲しい
select last_name from users where last_name like '中%';

# 漢字の'中'を含む苗字のユーザー一覧を取得して欲しい
select last_name from users where last_name like '%中%';

# 漢字の`子'で終わる苗字のユーザー一覧を取得して欲しい
select first_name from users where first_name like '%子';

# 漢字の`子'で終わり、三文字で終わる苗字のユーザー一覧を取得して欲しい
select first_name from users where first_name like '%子';
