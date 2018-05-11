# leadership_bot
Testing bot for managing leadership in the League

## DB struct
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| user  | varchar(50) | YES  |     | NULL    |                |
| role  | varchar(50) | YES  |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+

Created with : `create table members (id int not null auto_increment, user varchar(50), role varchar(50), primary key (id));`
