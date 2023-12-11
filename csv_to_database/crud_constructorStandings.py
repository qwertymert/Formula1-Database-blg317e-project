import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor_standings = pd.read_csv('data/constructorStandings.csv', encoding='ISO-8859-1')

def insert_constructor_standings(record):
    record = record.where(pd.notnull(record), None)
    insert_sql = "INSERT into constructor_standings values (%s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))


for i, record in df_constructor_standings.iterrows():
    insert_constructor_standings(record)
print("Constructor standings inserted")


mydb.commit()

mycursor.close()
mydb.close()
