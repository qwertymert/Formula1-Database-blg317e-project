import mysql.connector
import pandas as pd
import yaml
from math import ceil

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_pit_stops = pd.read_csv('data/pitStops.csv', encoding='ISO-8859-1')

def insert_pit_stops(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    # if record[-3] is not None:
    #     record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into pit_stops values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    
length = len(df_pit_stops)
try:
    for i, record in df_pit_stops.iterrows():
        insert_pit_stops(record)
        if i % (length // 5) == 0:
            print(str(ceil(i / length * 100)) + "%", "loaded")
    print("Pit stops inserted")
    print()
except mysql.connector.errors.IntegrityError as err:
    print("Pit stops already inserted")
except Exception as err:
    print(err)

mydb.commit()

mycursor.close()
mydb.close()
