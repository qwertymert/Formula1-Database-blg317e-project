import mysql.connector
import yaml

def read_table(table_name):
    db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
    mydb = mysql.connector.connect(**db_config)

    mycursor = mydb.cursor()
    
    mycursor.execute("SHOW COLUMNS FROM " + table_name)
    columns = mycursor.fetchall()
    mycursor.reset()
    
    mycursor.execute("SELECT * FROM " + table_name)
    myresult = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    
    return myresult, columns

def get_table_names():
    db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
    mydb = mysql.connector.connect(**db_config)

    mycursor = mydb.cursor()
    
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    
    return tables