import mysql.connector
import pandas as pd
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor_results = pd.read_csv('data/constructorResults.csv', encoding='ISO-8859-1')

def insert_constructor_results(record):
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into constructor_results values (%s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

try:
    for i, record in df_constructor_results.iterrows():
        insert_constructor_results(record)
    print("Constructor Results inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Constructor Results already inserted")
except Exception as err:
    print(err)
    
mydb.commit()

mycursor.close()
mydb.close()
