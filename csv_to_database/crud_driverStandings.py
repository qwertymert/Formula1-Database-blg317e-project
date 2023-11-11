import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="123mert*" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_driver_standings = pd.read_csv('data/driverStandings.csv', encoding='ISO-8859-1')


def insert_driver_standings(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "INSERT into driver_standings values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))


for i, record in df_driver_standings.iterrows():
    insert_driver_standings(record)
print("Driver_standings inserted")


mydb.commit()

mycursor.close()
mydb.close()
