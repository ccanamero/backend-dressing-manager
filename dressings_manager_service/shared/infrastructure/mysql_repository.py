
import mysql.connector

from dressings_manager_service.shared.infrastructure.errors import RepositoryNotFoundError


class MysqlRepository:
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str,
            table_name=str,
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database_name = database_name
        self.table_name = table_name # The table 'table_name'
        self._connect()

    def _connect(self):
        try:

            self.database_connection = mysql.connector.connect(host = self.host, database= self.database_name, user = self.user, password = self.password) #, connection_timeout = 10)
            
        except mysql.connector.Error:
            self.database_connection.rollback()
            raise RepositoryNotFoundError(f"Unable to connect to database at host={self.host}, port ={self.port}")


    def is_reachable(self):
        try:
            self.database_connection.get_server_info()
            return True
        except mysql.connector.Error:
            return False
