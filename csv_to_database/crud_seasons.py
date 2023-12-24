import mysql.connector
import pandas as pd
import yaml
from math import ceil

db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

mydb = mysql.connector.connect(**db_config)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_seasons = pd.read_csv('data/seasons.csv', encoding='ISO-8859-1')

def insert_seasons(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into seasons values (%s, %s)"
    mycursor.execute(insert_sql, tuple(record))

length = len(df_seasons)
try:
    for i, record in df_seasons.iterrows():
        insert_seasons(record)
        if i % (length // 5) == 0:
            print(str(ceil(i / length * 100)) + "%", "loaded")
    print("Seasons inserted")
except mysql.connector.errors.IntegrityError as err:
    print("Seasons already inserted")
except Exception as err:
    print(err)

mydb.commit()

mycursor.close()
mydb.close()
