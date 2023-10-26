import pandas as pd
from path.to.database import connect_to_database

def import_data(file_path, table_name, database_name):
    cnx, cursor = connect_to_database(database_name)
    data = pd.read_csv(file_path)
    data.to_sql(name=table_name, con=cnx, if_exists='append', index=False)
    cnx.close()