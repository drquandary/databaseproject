import tkinter as tk
from tkinter import ttk
import pandas as pd
from path.to.database import connect_to_database

class DatabaseGUI:
    def __init__(self, root, database_name):
        self.root = root
        self.database_name = database_name
        self.tree = ttk.Treeview(root)
        self.tree.pack()
        self.load_data()

    def load_data(self):
        cnx, cursor = connect_to_database(self.database_name)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for (table_name,) in cursor:
            self.tree.insert('', 'end', text=table_name)
        cnx.close()

root = tk.Tk()
gui = DatabaseGUI(root, 'your_database_name')
root.mainloop()