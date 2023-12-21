import mysql.connector
import yaml

def filter_table_and_column(table_name, column_name, value, value_type):
    db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
    mydb = mysql.connector.connect(**db_config)

    mycursor = mydb.cursor()
    
    if value_type == "string":
        sql = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%{value}%'"
    else:
        sql = f"SELECT * FROM {table_name} WHERE {column_name} = {value}"
        
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    
    return rows

def get_table_names():
    db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
    mydb = mysql.connector.connect(**db_config)

    mycursor = mydb.cursor()
    
    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    
    mycursor.close()
    mydb.close()
    
    return tables