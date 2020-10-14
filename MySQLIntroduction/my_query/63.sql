# 63 行を数える

use mydb;

# userが何人いるか教えて
select count(id) from users;

# userの内何人が女性か教えて
select count(id) from users where users.gender = 2;
