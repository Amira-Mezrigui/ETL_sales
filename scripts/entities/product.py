from entities.table_info import TableInfo

class Product (TableInfo):
    def __init__(self, url):
        super().__init__(
            url, 
            table_name='products', 
            primary_key='id'
            )
    
    def transform(self, products_df):
        columnsDict = {
            "ID Référence produit":"id",
            "Nom":"name",
            "Prix":"price",
            "Stock":"stock"
            }
        return TableInfo.transform(products_df, columnsDict)
        