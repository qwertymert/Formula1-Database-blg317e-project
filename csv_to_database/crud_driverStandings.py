import mysql.connector
import pandas as pd
import yaml

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_driver_standings = pd.read_csv('data/driverStandings.csv', encoding='ISO-8859-1')

def insert_driver_standings(record):
    record = record.where(pd.notnull(record), None)
    insert_sql = "INSERT into driver_standings values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

try:
    for i, record in df_driver_standings.iterrows():
        insert_driver_standings(record)
    print("Driver_standings inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Driver_standings already inserted")
except Exception as err:
    print(err)
    
mydb.commit()

mycursor.close()
mydb.close()
