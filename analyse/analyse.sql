
---- lechiffre d'affaires total
REPLACE INTO total_sale (total_sale) 
SELECT SUM(s.quantity*p.price) AS total_sale
FROM sales s
JOIN products p
    ON s.id_product=p.id;

----  les ventes par produit
REPLACE INTO product_sale (id_product,product_name,sale_per_product) 
SELECT p.id AS id_product, p.name AS product_name , SUM(s.quantity*p.price) AS sale_per_product
FROM sales s
JOIN products p
    ON s.id_product=p.id
GROUP BY (p.id);

---- les ventes par région
REPLACE INTO sale_city(id_shop,city,sale_per_city)
SELECT a.id_shop, a.city , SUM(s.quantity*p.price) AS sale_per_city
FROM sales s
JOIN products p
    ON s.id_product=p.id
JOIN shops a
    ON a.id_shop = s.id_shop
GROUP BY (a.id_shop);

/* *************************Données obtenus************************** 
sqlite> select * from sale_city;
1|Paris|799.8
2|Marseille|1009.73
3|Lyon|1059.79
4|Bordeaux|829.81
5|Lille|249.93
6|Nantes|739.83
7|Strasbourg|579.89

sqlite> select * from product_sale;
REF001|Produit A|1199.76
REF002|Produit B|539.73
REF003|Produit C|449.85
REF004|Produit D|1679.79
REF005|Produit E|1399.65

sqlite> select * from total_sale;  
5268.78 */

