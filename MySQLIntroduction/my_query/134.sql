# 134 テーブル構造の変更

use book_store;

-- show columns from books;

# 列の追加
-- alter table books add price int after id;
-- show columns from books;

# 列名の変更
-- alter table books change price unit_price int;
-- show columns from books;

# 列の削除
-- alter table books drop unit_price;
-- show columns from books;