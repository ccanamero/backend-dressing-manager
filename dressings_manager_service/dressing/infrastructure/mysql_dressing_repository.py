
from typing import List

from dressings_manager_service.dressing.domain.dressing import Dressing
from dressings_manager_service.dressing.domain.dressing_repository import DressingRepository
from dressings_manager_service.shared.infrastructure.mysql_repository import MysqlRepository

class MysqlDressingRepository(MysqlRepository, DressingRepository):
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


    def store(self, dressing: Dressing):
        insertQuery = "INSERT INTO dressings (id_, name_, type_, tissue_treating, exudate_compatibility, treated_location, fight_tunneling, fight_bad_olor, adhesive, hemostatic, instructions_to_use_es, instructions_to_use_gal, instructions_to_use_eng) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (dressing.id_, dressing.name, dressing.type_, dressing.tissue_treating, dressing.exudate_compatibility, dressing.treated_location, dressing.fight_tunneling, dressing.fight_bad_olor, dressing.adhesive, dressing.hemostatic, dressing.instructions_to_use_es, dressing.instructions_to_use_gal, dressing.instructions_to_use_eng)
        self.my_cursor.execute(insertQuery, values, True)
        self.database_connection.commit()

    # Update the dressing name and/or hospital name
    def update(self, dressing: Dressing):
        updateQuery = "UPDATE dressings SET name_ = %s, type_ = %s, tissue_treating = %s, exudate_compatibility = %s, treated_location = %s, fight_tunneling = %s, fight_bad_olor = %s, adhesive = %s, hemostatic = %s, instructions_to_use_es = %s, instructions_to_use_gal = %s, instructions_to_use_eng = %s WHERE id_ = %s"
        values = dressing.name, dressing.type_, dressing.tissue_treating, dressing.exudate_compatibility, dressing.treated_location, dressing.fight_tunneling, dressing.fight_bad_olor, dressing.adhesive, dressing.hemostatic, dressing.instructions_to_use_es, dressing.instructions_to_use_gal, dressing.instructions_to_use_eng, dressing.id_
        self.my_cursor.execute(updateQuery, values, True)
        self.database_connection.commit()

    def remove(self, dressing_id: str):
        removeQuery = "DELETE FROM dressings WHERE id_ = %s"
        values = dressing_id
        self.my_cursor.execute(removeQuery, (values,), True)
        self.database_connection.commit()

    def retrieve(self, id_: str) -> List[Dressing]:
        retrieveQuery = "SELECT * FROM dressings WHERE id_= %s"
        values = id_

        self.my_cursor.execute(retrieveQuery, (values,), True)
        records = self.my_cursor.fetchall()
        
        print("\nPrinting the dressing with id_ = ", id_)
        global a_id, a_name, a_type, a_tissue_treating, a_exudate_compatibility, a_treated_location, a_fight_tunneling, a_fight_bad_olor, a_adhesive, a_hemostatic, a_instructions_to_use_es, a_instructions_to_use_gal, a_instructions_to_use_eng
        a_id = ""
        a_name = "" 
        a_type=""
        a_tissue_treating = ""
        a_exudate_compatibility = "" 
        a_treated_location = "" 
        a_fight_tunneling = "" 
        a_fight_bad_olor = ""
        a_adhesive = "" 
        a_hemostatic = "" 
        a_instructions_to_use_es = ""
        a_instructions_to_use_gal = "" 
        a_instructions_to_use_eng = ""
        for row in records:
            print("Id_ = ", row[0], )
            print("Name = ", row[1], )
            print("Type = ", row[2], )
            print("Tejido = ", row[3], )
            print("Compatibilidad del exudado = ", row[4], )
            print("Loclaización del objetivo = ", row[5], )
            print("Lucha contra el tunelamiento = ", row[6], )
            print("Lucha contra el mal olor = ", row[7], )
            print("Adhesivo = ", row[8], )
            print("Hemostático = ", row[9], )
            print("Instructions in Español = ", row[10], )
            print("Instructions in Gallego = ", row[11], )
            print("Instructions in English = ", row[12], "\n")
            a_id = row[0]
            a_name = row[1]
            a_type = row[2]
            a_tissue_treating = row[3]
            a_exudate_compatibility = row[4] 
            a_treated_location = row[5]
            a_fight_tunneling = row[6]
            a_fight_bad_olor = row[7]
            a_adhesive = row[8]
            a_hemostatic = row[9]
            a_instructions_to_use_es = row[10]
            a_instructions_to_use_gal = row[11]
            a_instructions_to_use_eng = row[12]
            
        a_dressing = Dressing(a_id, a_name, a_type,a_tissue_treating, a_exudate_compatibility, a_treated_location, a_fight_tunneling, a_fight_bad_olor, a_adhesive, a_hemostatic, a_instructions_to_use_es, a_instructions_to_use_gal, a_instructions_to_use_eng)
            
        self.database_connection.commit()
        return a_dressing

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
        self.dressing.delete_many({}) """


