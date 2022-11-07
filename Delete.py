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


# delete a record from table
delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""
execute_query(connection, delete_course)


# remove a column from table
delete_column = """
ALTER TABLE client
DROP COLUMN industry;
"""
execute_query(connection, delete_column)


# drops table
drop_table = """
DROP TABLE takes_course
"""
execute_query(connection, drop_table)


# drops schema
drop_db = """
DROP SCHEMA School
"""
execute_query(connection, drop_db)