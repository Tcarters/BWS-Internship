---CREATE A NEW TABLE `shop` ---
CREATE TABLE shop(
    ID INTEGER,
    Product_name VARCHAR(255),
    Price DECIMAL (4,3),
    Details VARCHAR(255),
    Items_sold INTEGER DEFAULT 0);
);

---INSERT 5 products into table
INSERT INTO shop(ID, Product_name, Price, Details, Items_sold) VALUES 
    (1, 'Milk', 20.10, 'Best Milk'),
    (2, 'Coffee', 5.50, 'Nice coffee', 3),
    (3, 'Bread', 20, 'Sugar Bread', 10),
    (4, 'Sugar', 14.50, 'Cube Sugar', 0),
    (5, 'Chocolate', 9.75, 'Fresh Choco', 4);


--- SELECT 3 products from the Table;
SELECT * from shop where id <= 3;