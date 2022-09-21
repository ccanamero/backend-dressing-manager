
from typing import List

from dressings_manager_service.protection.domain.protection import Protection
from dressings_manager_service.protection.domain.protection_repository import ProtectionRepository
from dressings_manager_service.shared.infrastructure.mysql_repository import MysqlRepository

class MysqlProtectionRepository(MysqlRepository, ProtectionRepository):
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str
    ):
        super().__init__(
            host,
            port,
            user,
            password,
            database_name
        )
        
        self.my_cursor = self.database_connection.cursor()


    def store(self, protection: Protection):
        insertQuery = "INSERT INTO protections (id_, name_, type_) VALUES (%s, %s, %s)"
        values = (protection.id_, protection.name, protection.type_)
        self.my_cursor.execute(insertQuery, values, True)
        self.database_connection.commit()

    # Update the protection name and/or hospital name
    def update(self, protection: Protection):
        updateQuery = "UPDATE protections SET name_ = %s, type_ = %s WHERE id_ = %s"
        values = protection.name, protection.type_, protection.id_
        self.my_cursor.execute(updateQuery, values, True)
        self.database_connection.commit()

    def remove(self, protection_id: str):
        removeQuery = "DELETE FROM protections WHERE id_ = %s"
        values = protection_id
        self.my_cursor.execute(removeQuery, (values,), True)
        self.database_connection.commit()

    def retrieve(self, id_: str) -> List[Protection]:
        retrieveQuery = "SELECT * FROM protections WHERE id_= %s"
        values = id_

        self.my_cursor.execute(retrieveQuery, (values,), True)
        records = self.my_cursor.fetchall()
        
        print("\nPrinting the protection with id_ = ", id_)
        global a_id, a_name, a_type
        a_id = ""
        a_name = "" 
        a_type=""
        for row in records:
            print("Id_ = ", row[0], )
            print("Name = ", row[1], )
            print("Type = ", row[2], "\n")
            a_id = row[0]
            a_name = row[1]
            a_type= row[2]
            
        a_protection = Protection(a_id, a_name, a_type)
            
        self.database_connection.commit()
        return a_protection

    def _commit_and_close_connection(self):
        # Commit the changes
        self.database_connection.commit()
        # Closing database connection
        self.my_cursor.close()
        self.database_connection.close()

    













"""      def retrieveAll(self) -> List[Collagenase]:
        records = self.my_cursor.fetchall()
        print("Total number of rows in table: ", self.my_cursor.rowcount)

        retrieveQuery = "SELECT * FROM collagenase"
        values = id_
        self.my_cursor.execute(retriveQuery, values)

        print("\nPrinting each collagenase")
        for row in records:
            print("Id_ = ", row[0], )
            print("Name = ", row[1], "\n")
            
        # Falta meter los valores en collagenasas
        return collagenases 

    def empty(self):
        self.protection.delete_many({}) """


