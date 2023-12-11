import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor_results = pd.read_csv('data/constructorResults.csv', encoding='ISO-8859-1')

def insert_constructor_results(record):
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into constructor_results values (%s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))


for i, record in df_constructor_results.iterrows():
    insert_constructor_results(record)
print("Constructor Results inserted")


mydb.commit()

mycursor.close()
mydb.close()
