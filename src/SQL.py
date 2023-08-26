import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


class SQLDatabase:
    def __init__(self):
        self.db_username = "root"
        self.db_password = 2655
        self.db_host = "localhost"
        self.db_port = 3306
        self.db_name = "students"
        self.metadata = ""
        self.engine = ""

    def create_connection(self):
        db_url = f"mysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        self.engine = create_engine(db_url)
        self.metadata = MetaData(self.engine)

    def create_table(self):
            table_name = "laptop_data"
            table = Table(
            table_name,
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("Product_Name", String(255)),
            Column("Prices", String(50)),
            Column("Description", String(500)),
            Column("Review", String(500))
        )
            self.metadata.create_all()
    
    def insert_data(self, table_name, data):
         data.to_sql(table_name, con=self.engine, if_exists="replace", index=False)



#pip install mysqlclient

