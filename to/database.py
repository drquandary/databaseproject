import mysql.connector
from mysql.connector import errorcode

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