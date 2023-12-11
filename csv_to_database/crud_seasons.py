import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_seasons = pd.read_csv('data/seasons.csv', encoding='ISO-8859-1')

print(df_seasons.columns)

def insert_seasons(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into seasons values (%s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_seasons.iterrows():
    insert_seasons(record)
print("Seasons inserted")


mydb.commit()

mycursor.close()
mydb.close()
