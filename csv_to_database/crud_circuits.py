import mysql.connector
import pandas as pd
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_circuits = pd.read_csv('data/circuits.csv', encoding='ISO-8859-1')

def insert_circuits(record):    
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into circuits values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

try:
    for i, record in df_circuits.iterrows():
        insert_circuits(record)
    print("Circuits inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Circuits already inserted")
except Exception as err:
    print(err)
    
mydb.commit()

mycursor.close()
mydb.close()
