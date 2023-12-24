import mysql.connector
import pandas as pd
import yaml
from math import ceil

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_results = pd.read_csv('data/results.csv', encoding='ISO-8859-1')

def insert_results(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)

    # Convert 'fastestLapTime' column to the desired format
    
    # if record['fastestLapTime'] is not None:
    #     record['fastestLapTime'] = pd.to_datetime(record['fastestLapTime']).strftime('%H:%M:%S')

    insert_sql = "INSERT INTO results VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

length = len(df_results)
try:
    for i, record in df_results.iterrows():
        insert_results(record)
        if i % (length // 5) == 0:
            print(str(ceil(i / length * 100)) + "%", "loaded")
    print("Results inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Results already inserted")
except Exception as err:
    print(err)

mydb.commit()

mycursor.close()
mydb.close()
