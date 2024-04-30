CREATE TABLE IF NOT EXISTS products(
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS shops(
    id_shop INTEGER PRIMARY KEY,
    city TEXT NOT NULL,
    salaries INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS sales(
    `date` TEXT NOT NULL,
    id_product TEXT,
    quantity INTEGER NOT NULL,
    id_shop INTEGER,
    PRIMARY KEY (`date`, id_product, id_shop),
    FOREIGN KEY(id_product) REFERENCES products(id),
    FOREIGN KEY(id_shop) REFERENCES shops(id_shop)
);

--------- Analyse tables
CREATE TABLE IF NOT EXISTS total_sale(
    total_sale FLOAT PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS product_sale(
    id_product TEXT PRIMARY KEY,
    product_name TEXT,
    sale_per_product FLOAT,
    FOREIGN KEY(id_product) REFERENCES products(id)
);
CREATE TABLE IF NOT EXISTS sale_city(
    id_shop INTEGER PRIMARY KEY,
    city TEXT,
    sale_per_city FLOAT,
    FOREIGN KEY(id_shop) REFERENCES shops(id_shop)

);
