import tkinter as tk
from tkinter import ttk
import mysql.connector
from mysql.connector import errorcode
import pandas as pd

def create_database(cursor, database_name):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(database_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def connect_to_database(database_name):
    cnx = mysql.connector.connect(user='your_username', password='your_password')
    cursor = cnx.cursor()
    try:
        cnx.database = database_name    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, database_name)
            cnx.database = database_name
        else:
            print(err)
            exit(1)
    return cnx, cursor

def import_data(file_path, table_name, database_name):
    cnx, cursor = connect_to_database(database_name)
    data = pd.read_csv(file_path)
    data.to_sql(name=table_name, con=cnx, if_exists='append')
    cnx.close()

class DatabaseGUI:
    def __init__(self, root, database_name):
        self.root = root
        self.database_name = database_name
        self.tree = ttk.Treeview(root)
        self.tree.pack()
        self.load_data()

    def load_data(self):
        cnx, cursor = connect_to_database(self.database_name)
        cursor.execute("SHOW TABLES")
        for (table_name,) in cursor:
            self.tree.insert('', 'end', text=table_name)
        cnx.close()

root = tk.Tk()
gui = DatabaseGUI(root, 'your_database_name')
root.mainloop()