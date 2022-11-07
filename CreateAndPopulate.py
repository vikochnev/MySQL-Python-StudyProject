import mysql.connector
from mysql.connector import Error
import create_and_pop_queries as dt
import password


# reusable function to create server connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# reusable function to create database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# reusable function to connect to db
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


# creates DB and connects to it
pw = password.pw
db = "school"
connection = create_server_connection("localhost", "root", pw)
create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)
connection = create_db_connection("localhost", "root", pw, db)


# creates tables
execute_query(connection, dt.create_teacher_table)
execute_query(connection, dt.create_client_table)
execute_query(connection, dt.create_participant_table)
execute_query(connection, dt.create_course_table)

# adds relations (via foreign keys) to tables
execute_query(connection, dt.alter_participant)
execute_query(connection, dt.alter_course)
execute_query(connection, dt.alter_course_again)
execute_query(connection, dt.create_takescourse_table)

# populates tables
execute_query(connection, dt.pop_teacher)
execute_query(connection, dt.pop_client)
execute_query(connection, dt.pop_participant)
execute_query(connection, dt.pop_course)
execute_query(connection, dt.pop_takescourse)
