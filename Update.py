import mysql.connector
from mysql.connector import Error
import password


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# reusable function to execute queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


pw = password.pw
db = "school"
connection = create_db_connection("localhost", "root", pw, db)

# sample update query:
print("Entry before update:")
q1 = """
SELECT * 
FROM client
WHERE client_id = 101;
"""
results = read_query(connection, q1)
for result in results:
    print(result)

update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""
execute_query(connection, update)

print("Entry after update:")
q2 = """
SELECT * 
FROM client
WHERE client_id = 101;
"""
results = read_query(connection, q2)
for result in results:
    print(result)