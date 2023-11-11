import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="123mert*" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_races = pd.read_csv('data/races.csv', encoding='ISO-8859-1')

print(df_races.columns)

def insert_races(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    if record[-3] is not None:
        record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into races values (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_races.iterrows():
    insert_races(record)
print("Races inserted")


mydb.commit()

mycursor.close()
mydb.close()
