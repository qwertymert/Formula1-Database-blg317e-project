import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_lap_times = pd.read_csv('data/lapTimes.csv', encoding='ISO-8859-1')

print(df_lap_times.columns)

def insert_lap_times(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    # if record[-3] is not None:
    #     record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into lap_times values (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_lap_times.iterrows():
    insert_lap_times(record)
print("Lap times inserted")


mydb.commit()

mycursor.close()
mydb.close()
