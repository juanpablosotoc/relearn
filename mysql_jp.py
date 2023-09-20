from mysql import connector

connection_args = {
    'user': 'root',
    'host': 'localhost',
    'password': 'Joaqo1664',
    'database': 'wayne_foundation',
    'buffered': True
}


class Mysql_fnc:
    def __init__(self, fnc) -> None:
        self.no_connect = fnc

    def connect(self, **kwargs):
        try:
            connection = connector.connect(**connection_args)
            if connection.is_connected():
                print('mysql session started')
                cursor = connection.cursor(dictionary=True) 
                return {'error': False, 'data': self.no_connect(connection=connection, cursor=cursor, **kwargs)}
        except connector.Error as e:
            connection.rollback()
            print(e)
            return {'error': True, 'data': e}
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print('mysql session ended')


def mysql_decorate(fnc):
    return Mysql_fnc(fnc)