
from typing import List

from dressings_manager_service.collagenase.domain.collagenase import Collagenase
from dressings_manager_service.collagenase.domain.collagenase_repository import CollagenaseRepository
from dressings_manager_service.shared.infrastructure.mysql_repository import MysqlRepository

class MysqlCollagenaseRepository(MysqlRepository, CollagenaseRepository):
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


    def store(self, collagenase: Collagenase):
        insertQuery = "INSERT INTO collagenases (id_, name_) VALUES (%s, %s)"
        values = (collagenase.id_, collagenase.name)
        self.my_cursor.execute(insertQuery, values, True)
        self.database_connection.commit()


    # Thinking about this functionality because collagenase only has two attributes: id and name
    def update(self, collagenase: Collagenase):
        updateQuery = "UPDATE collagenases SET name_ = %s WHERE id_ = %s"
        values = collagenase.name, collagenase.id_
        self.my_cursor.execute(updateQuery, values, True)
        self.database_connection.commit()


    def remove(self, collagenase_id: str):
        removeQuery = "DELETE FROM collagenases WHERE id_ = %s"
        values = collagenase_id
        
        self.my_cursor.execute(removeQuery, (values,), True)
        self.database_connection.commit()

    def retrieve(self, id_: str) -> List[Collagenase]:
        retrieveQuery = "SELECT * FROM collagenases WHERE id_= %s"
        values = id_

        self.my_cursor.execute(retrieveQuery, (values,), True)
        records = self.my_cursor.fetchall()
        
        print("\nPrinting the collagenase with id_ = ", id_)
        global a_id, a_name
        a_id = ""
        a_name = ""
        for row in records:
            print("Id_ = ", row[0], )
            print("Name = ", row[1], "\n")
            a_id = row[0]
            a_name = row[1]
            
        a_collagenase = Collagenase(a_id, a_name)
            
        self.database_connection.commit()
        return a_collagenase

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
        self.collection.delete_many({}) """


