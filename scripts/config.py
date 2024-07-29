BASE_URL= 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSawI56WBC64foMT9pKCiY594fBZk9Lyj8_bxfgmq-8ck_jw1Z49qDeMatCWqBxehEVoM6U1zdYx73V'

def build_url(id, base_url=BASE_URL):
   return f"{base_url}/pub?gid={id}&single=true&output=csv"
   

PRODUCT_URL = build_url(id=0)
SHOPS_URL = build_url(id='714623615')
SALES_URL = build_url(id='760830694')

SCHEMA_CREATION_SCRIPT_PATH = '../schema/schema.sql'
ANALYSIS_SQL_SCRIPT_PATH = '../analyse/analyse.sql'

DATABASE_PATH = '/database/sales.db'