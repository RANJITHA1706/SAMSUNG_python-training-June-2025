import pymysql

class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.location = location

    def __str__(self):
        return f'Name:{self.name}, Location:{self.location}'

class Db_operations:
    def connect_db(self):
        try:
            connection = pymysql.Connect(
                host='localhost',
                port=3306,
                user='root',
                password='Forest#321',
                database='db1',
                charset='utf8'
            )
            print('DB connected')
            return connection
        except:
            print('DB connection failed')

    def disconnect_db(self, connection):
        try:
            connection.close()
            print('DB dis-connected')
        except:
            print('Error while disconnecting DB')

    def create_table(self):
        connection = self.connect_db()
        query = """
            CREATE TABLE IF NOT EXISTS persons (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(32) NOT NULL,
                gender CHAR(1) CHECK(gender IN ('m','M','f','F')),
                dob DATE,
                location VARCHAR(32)
            );
        """
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        print('Table created')
        self.disconnect_db(connection)

    def insert_row(self, person):
        query = 'INSERT INTO persons(name, gender, dob, location) VALUES(%s, %s, %s, %s);'
        person_tuple = (person.name, person.gender, person.dob, person.location)
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, person_tuple)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return self.get_latest_row_id()

    def update_row(self, data):
        query = 'UPDATE persons SET name = %s, gender = %s, dob = %s, location = %s WHERE id = %s'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def delete_row(self, id):
        query = f'DELETE FROM persons WHERE id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            print(f'Person with id = {id} deleted')
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)

    def search_row(self, id):
        row = None
        query = f'SELECT * FROM persons WHERE id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            row = cursor.fetchone()
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        return row

    def list_all_rows(self):
        query = 'SELECT * FROM persons;'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        rows = []
        if count == 0:
            print('No rows found')
        else:
            rows = cursor.fetchall()
        cursor.close()
        self.disconnect_db(connection)
        return rows

    def get_latest_row_id(self):
        query = 'SELECT MAX(id) FROM persons;'
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        id = cursor.fetchone()
        cursor.close()
        self.disconnect_db(connection)
        return id[0]

				

