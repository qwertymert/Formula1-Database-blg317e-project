import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_constructor = pd.read_csv('data/constructors.csv', encoding='ISO-8859-1')

print(df_constructor.columns)

def insert_constructors(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)
    insert_sql = "insert into constructors values (%s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))
    


for i, record in df_constructor.iterrows():
    insert_constructors(record)
print("Constructors inserted")


mydb.commit()

mycursor.close()
mydb.close()
