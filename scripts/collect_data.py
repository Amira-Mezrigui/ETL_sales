import pandas as pd
import sqlite3

def create_schema(db):
    #To read the content of sql file
    with open('../schema/schema.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    #Exécute schema.sql
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()

# Function To insert Data
def insert_data(df, table_name, primary_key, db):
    cursor = db.cursor()
    for row in df.to_records(index=False):
        query = f"""
            INSERT INTO {table_name} 
            VALUES {row} ON CONFLICT ({primary_key}) DO NOTHING
            """
        cursor.executescript(query)
        db.commit()

# products data transform
def transform_products(products_df):
    columns = {"ID Référence produit":"id","Nom":"name","Prix":"price","Stock":"stock"}
    products_df.rename(columns = columns, inplace=True)
    return products_df[columns.values()] 

# shops data transform
def transform_shops(shops_df):
    columns = {"ID Magasin":"id_shop","Ville":"city","Nombre de salariés":"salaries"}
    shops_df.rename(columns = columns, inplace=True)
    return shops_df[columns.values()] 

# sales data transform
def transform_sales(sales_df):
    columns = {"Date":"date","ID Référence produit":"id_product","Quantité":"quantity", "ID Magasin":"id_shop"}
    sales_df.rename(columns = columns, inplace=True)
    return sales_df[columns.values()] 

# Analyse data
def analyse_data(db):
    with open('../analyse/analyse.sql', 'r') as sql_file:
        sql_script = sql_file.read()
    #Exécute analyse.sql
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()



url_products = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=0&single=true&output=csv"
url_shops = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=714623615&single=true&output=csv"
url_sales = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V/pub?gid=760830694&single=true&output=csv"


products_df = pd.read_csv(url_products)
shops_df = pd.read_csv(url_shops)
sales_df = pd.read_csv(url_sales)
#connection with database
db = sqlite3.connect('/data/sales.db')
    
create_schema(db)

transformed_products_df = transform_products(products_df)
insert_data( df=transformed_products_df, table_name="products", primary_key="id", db=db)

transformed_shops_df = transform_shops(shops_df)
insert_data(df=transformed_shops_df, table_name="shops", primary_key="id_shop", db=db)

transformed_sales_df = transform_sales(sales_df)
insert_data(df=transformed_sales_df, table_name="sales", primary_key="sales.date, sales.id_product, sales.id_shop", db=db)  

analyse_data(db)

db.close()