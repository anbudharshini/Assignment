import mysql.connector
from util.dbpropertyutil import DBPropertyUtil

class DBConn:
    @staticmethod
    def get_connection():
        props = DBPropertyUtil.get_connection_properties()
        if not props:
            raise Exception("Connection properties could not be loaded.")

        try:
            connection = mysql.connector.connect(
                host=props['host'],
                user=props['user'],
                password=props['password'],
                database=props['database']
            )
            if connection.is_connected():
                return connection
        except mysql.connector.Error as e:
            print(f"MySQL error: {e}")
        except Exception as ex:
            print(f"Unexpected error: {ex}")
        return None
