import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="123mert*" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_driver = pd.read_csv('data/drivers.csv', encoding='ISO-8859-1')

print(df_driver.columns)

def insert_drivers(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    if record[-3] is not None:
        record[-3] = pd.to_datetime(record[-3]).strftime('%Y-%m-%d')
    insert_sql = "insert into drivers values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_driver.iterrows():
    insert_drivers(record)
print("Drivers inserted")


mydb.commit()

mycursor.close()
mydb.close()
