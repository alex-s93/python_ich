import mysql.connector


def create_connection(**config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
    return result
