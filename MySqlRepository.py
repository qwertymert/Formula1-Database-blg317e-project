import mysql.connector
import yaml

class MySQLRepository:
    def __init__(self):
        self.db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        self.connection = mysql.connector.connect(**self.db_config)

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def execute_update(self, query, params=None):
        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()

    def create(self, table_name, data):
        columns = ', '.join(data.keys())
        values = ', '.join(['%s' for _ in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.execute_update(query, tuple(data.values()))

    def read(self, table_name, condition=None):
        if condition:
            query = f"SELECT * FROM {table_name} WHERE {condition}"
        else:
            query = f"SELECT * FROM {table_name}"
        return self.execute_query(query)

    def update(self, table_name, data, condition):
        set_clause = ', '.join([f"{key}=%s" for key in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.execute_update(query, tuple(data.values()))

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_update(query)

    def get_columns(self, table_name):
        query = f"SHOW COLUMNS FROM {table_name}"
        columns = self.execute_query(query)
        return [column[0] for column in columns]


    def read_table(table_name):
        db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        mydb = mysql.connector.connect(**db_config)

        mycursor = mydb.cursor()
        
        mycursor.execute("SHOW COLUMNS FROM " + table_name)
        columns = mycursor.fetchall()
        mycursor.reset()
        
        mycursor.execute("SELECT * FROM " + table_name)
        myresult = mycursor.fetchall()
        
        mycursor.close()
        mydb.close()
        
        return myresult, columns

    def read_columns(table_name):
        db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        mydb = mysql.connector.connect(**db_config)

        mycursor = mydb.cursor()
        
        mycursor.execute("SHOW COLUMNS FROM " + table_name)
        columns = mycursor.fetchall()
        
        mycursor.close()
        mydb.close()
        
        return columns

    def get_table_names():
        db_config = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
        mydb = mysql.connector.connect(**db_config)

        mycursor = mydb.cursor()
        
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()
        
        mycursor.close()
        mydb.close()
        
        return tables