class TableInfo:
    def __init__(self,
                 url,
                 table_name,
                 primary_key):
        self.url = url
        self.table_name = table_name
        self.primary_key = primary_key
    
    def transform(df, columns):
        df.rename(columns = columns, inplace=True)
        return df[columns.values()]