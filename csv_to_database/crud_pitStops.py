import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_pit_stops = pd.read_csv('data/pitStops.csv', encoding='ISO-8859-1')

print(df_pit_stops.columns)

def insert_pit_stops(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    # if record[-3] is not None:
    #     record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into pit_stops values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_pit_stops.iterrows():
    insert_pit_stops(record)
print("Pit stops inserted")


mydb.commit()

mycursor.close()
mydb.close()
