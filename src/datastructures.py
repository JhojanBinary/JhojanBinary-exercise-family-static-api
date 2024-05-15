"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
                            {
                                "id": self._generateId(),
                                "first_name": "John",
                                "last_name": self.last_name,
                                "age": 33,
                                "lucky_numbers": [7, 13, 22]
                            },
                           {
                                "id": self._generateId(),
                                "first_name": "Jane",
                                "last_name": self.last_name,
                                "age": 35,
                                "lucky_numbers": [10, 14, 3]
                            },
                            {
                                "id": self._generateId(),
                                "first_name": "Jimmy",
                                "last_name": self.last_name,
                                "age": 5,
                                "lucky_numbers": [1]
                            }
                        ]
    # Solo lectura: Usa este método para generar IDs de miembros aleatorios al agregar miembros a la lista    
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)



    def add_member(self, member):
        self._members.append(member)




    def delete_member(self, id):
    # Find the index of the member with the given ID
    # Encuentra el índice del miembro con el ID dado
        index_to_remove = None
        for i, member in enumerate(self._members):
            if member["id"] == id:
                index_to_remove = i
                break
        # If the member is found, remove it from the list
        # Si se encontró el miembro, elimínalo de la lista
        if index_to_remove is not None:
            del self._members[index_to_remove]
            return {"msg":  "id" + id + "deleted", "status_code": 200}
        else:
            return {"msg": "id" + id +  "not found", "status_code": 404}




    def get_member(self, id):
        # If the member is found, remove it from the list
        # Busca el miembro con el ID dado
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    


    # Este método está hecho, devuelve una lista con todos los miembros de la familia
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members