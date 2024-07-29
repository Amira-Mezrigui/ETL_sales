from entities.table_info import TableInfo

class Shops (TableInfo):
    def __init__(self, url) -> None:
        super().__init__(
            url, 
            table_name='shops', 
            primary_key='id_shop'
            )
    
    def transform(self, shops_df):
        columns = {
            "ID Magasin":"id_shop",
            "Ville":"city",
            "Nombre de salariés":"salaries"
            }
        return TableInfo.transform(shops_df, columns)