SELECT * FROM table_name ORDER BY column_name DESC / ASC;

/*  DESC => means in descending Order
    ASC => means in ascending Order
 */

 ------------- selecting particular data rows -----------
 SELECT * FROM table_name WHERE id=5;

 SELECT * from table_name where id > 4;
 SELECT * from demo WHERE ID=1 OR ID=3 OR ID=5;
 SELECT * FROM demo WHERE ID=1 AND NAME='test';

---------------ORdering selected data-----------------
 SELECT * FROM demo WHERE ID > 3 ORDER BY ID DESC:
 SELECT * FROM demo WHERE ID > 1 AND ID < 5 ORDER BY NAME ASC;


 ---------------Limiting Data ----------------------------
 SELECT * FROM demo WHERE ID > 2 AND ID <= 5 ORDER BY ID ASC LIMIT 1; /* Limit here point to the row no to display */

 -----Insert new row- -------
 INSERT INTO table_name(name, hint) values('Kalob', 'Your teacher');

 -------UPDATE-----------
 UPDATE table_name SET NAME='name1' WHERE id=2;

 ---DELETE data-------
 DELETE from table_name WHERE id=10 or id=3;

 ----CREATE TABLE----
 CREATE TABLE table_name(id INTEGER, item_name VARCHAR(30), 
    price DECIMAL(5,2), 
    notes VARCHAR(255), 
    items_sold INTEGER DEFAULT 0 );

-------=-==-----TRUCATING DATA--------------------- means clean all data inside Table
TRUNCATE table_name;

----------------------DELETE A TABLE----------------
DROP TABLE table_name;
