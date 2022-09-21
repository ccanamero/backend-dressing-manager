
from typing import List

from dressings_manager_service.collection.domain.collection import Collection
from dressings_manager_service.collection.domain.collection_repository import CollectionRepository
from dressings_manager_service.shared.infrastructure.mysql_repository import MysqlRepository

class MysqlCollectionRepository(MysqlRepository, CollectionRepository):
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


    def store(self, collection: Collection):
        insertQuery = "INSERT INTO collections (id_, name_, hospital) VALUES (%s, %s, %s)"
        values = (collection.id_, collection.name, collection.hospital)
        self.my_cursor.execute(insertQuery, values, True)
        self.database_connection.commit()

    # Update the collection name and/or hospital name
    def update(self, collection: Collection):
        updateQuery = "UPDATE collections SET name_ = %s, hospital = %s WHERE id_ = %s"
        values = collection.name, collection.hospital, collection.id_
        self.my_cursor.execute(updateQuery, values, True)
        self.database_connection.commit()

    def remove(self, collection_id: str):
        removeQuery = "DELETE FROM collections WHERE id_ = %s"
        values = collection_id
        self.my_cursor.execute(removeQuery, (values,), True)
        self.database_connection.commit()

    def retrieve(self, id_: str) -> List[Collection]:
        retrieveQuery = "SELECT * FROM collections WHERE id_= %s"
        values = id_

        self.my_cursor.execute(retrieveQuery, (values,), True)
        records = self.my_cursor.fetchall()
        
        print("\nPrinting the collection with id_ = ", id_)
        global a_id, a_name, a_hospital
        a_id = ""
        a_name = "" 
        a_hospital=""
        for row in records:
            print("Id_ = ", row[0], )
            print("Name = ", row[1], )
            print("Hospital = ", row[2], "\n")
            a_id = row[0]
            a_name = row[1]
            a_hospital = row[2]
            
        a_collection = Collection(a_id, a_name, a_hospital)
            
        self.database_connection.commit()
        return a_collection

    def _commit_and_close_connection(self):
        # Commit the changes
        self.database_connection.commit()
        # Closing database connection
        self.my_cursor.close()
        self.database_connection.close()

"""     def retrieveAll(self) -> List[Collection]:
        retrieveQuery = "SELECT * FROM collections"
        self.my_cursor.execute(retrieveQuery)

        records = self.my_cursor.fetchall()
        print("Total number of rows in table: ", self.my_cursor.rowcount)

        print("\nPrinting each collection:")
        global a_id, a_name, a_hospital
        a_id = ""
        a_name = "" 
        a_hospital=""
        global collections
        collections=Collection("", "", "")
        for row in records:
            print(row)
            print("\n")
            print("Id_ = ", row[0], )
            print("Name = ", row[1], )
            print("Hospital = ", row[2], "\n")
            a_collection = Collection(a_id, a_name, a_hospital)
            collections.append(a_collection)

        self.database_connection.commit()
        return collections """






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


