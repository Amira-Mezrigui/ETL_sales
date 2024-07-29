from config import PRODUCT_URL, SHOPS_URL, SALES_URL, ANALYSIS_SQL_SCRIPT_PATH, SCHEMA_CREATION_SCRIPT_PATH, DATABASE_PATH
from entities.sales import Sales
from entities.shops import Shops
from entities.product import Product
from entities.table_info import TableInfo
import pandas as pd
import sqlite3
import logging

logger = logging.getLogger(__name__)

# Function To insert Data
def insert_data(df, table_name, primary_key, db):
    print(f"Inserting data in table {table_name}")
    cursor = db.cursor()
    for row in df.to_records(index=False):
        query = f"""
            INSERT INTO {table_name} 
            VALUES {row} ON CONFLICT ({primary_key}) DO NOTHING
            """
        print(f"Query to run {query}")
        cursor.executescript(query)
        db.commit()

# Read and execute an sql file
def execute_sql_script(db, file_path):
    #To read the content of sql file
    with open(file_path, 'r') as sql_file:
        sql_script = sql_file.read()
    #Exécute schema.sql
    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()

# read , transform and load data 
def etl(table_info: TableInfo, db):
    #read dataframe from csv and load it into a dataframe
    df = pd.read_csv(table_info.url)
    # transorm the format of dataframe
    transformed_df = table_info.transform(df)
    # insert data to the database
    insert_data( 
        transformed_df, 
        table_name=table_info.table_name, 
        primary_key=table_info.primary_key,
        db=db
        )

def main():
    sources = [
        Product(url=PRODUCT_URL),
        Shops(url=SHOPS_URL),
        Sales(url=SALES_URL),
    ]
    
    #create connection with database
    db = sqlite3.connect(DATABASE_PATH)

    # create the database schema
    execute_sql_script(db, SCHEMA_CREATION_SCRIPT_PATH)

    for source in sources:
        etl(source, db)

    # Create the analyse data
    execute_sql_script(db, ANALYSIS_SQL_SCRIPT_PATH)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    main()