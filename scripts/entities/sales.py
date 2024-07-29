from entities.table_info import TableInfo


class Sales (TableInfo):
    def __init__(self, url) -> None:
        super().__init__(
            url, 
            table_name='sales', 
            primary_key='sales.date, sales.id_product, sales.id_shop'
            )
    
    def transform(self, sales_df):
        columns = {
            "Date":"date",
            "ID Référence produit":"id_product",
            "Quantité":"quantity", 
            "ID Magasin":"id_shop"
            }
        return TableInfo.transform(sales_df, columns)
    