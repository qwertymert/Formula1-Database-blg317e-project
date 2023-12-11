import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="MyNewPass" # Change with your root password
)

mycursor = mydb.cursor()
mycursor.execute("use FORMULA1")

df_results = pd.read_csv('data/results.csv', encoding='ISO-8859-1')

print(df_results.columns)

def insert_results(record):
    # Replace pandas NaN with SQL NULL
    record = record.where(pd.notnull(record), None)

    # Convert 'fastestLapTime' column to the desired format
    
    # if record['fastestLapTime'] is not None:
    #     record['fastestLapTime'] = pd.to_datetime(record['fastestLapTime']).strftime('%H:%M:%S')

    insert_sql = "INSERT INTO results VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(insert_sql, tuple(record))

for i, record in df_results.iterrows():
    insert_results(record)
print("Results inserted")


mydb.commit()

mycursor.close()
mydb.close()
