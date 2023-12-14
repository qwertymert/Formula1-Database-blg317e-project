import mysql.connector
import pandas as pd
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor_standings = pd.read_csv('data/constructorStandings.csv', encoding='ISO-8859-1')

def insert_constructor_standings(record):
    record = record.where(pd.notnull(record), None)
    insert_sql = "INSERT into constructor_standings values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

try:
    for i, record in df_constructor_standings.iterrows():
        insert_constructor_standings(record)
    print("Constructor standings inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Constructor standings already inserted")
except Exception as err:
    print(err)



mydb.commit()

mycursor.close()
mydb.close()
