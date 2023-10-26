import sqlite3

def connect_to_database(database_name):
    cnx = sqlite3.connect(database_name)
    cursor = cnx.cursor()
    return cnx, cursor