import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="123mert*" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_circuits = pd.read_csv('data/circuits.csv', encoding='ISO-8859-1')

def insert_circuits(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into circuits values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))


for i, record in df_circuits.iterrows():
    insert_circuits(record)
print("Circuits inserted")


mydb.commit()

mycursor.close()
mydb.close()
