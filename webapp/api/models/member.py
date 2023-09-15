import json
import os
from collections import namedtuple



class Member():
    def __init__(self, input):
        self.__dict__.update(input)
    '''
    def __init__(self, student_id, name, role, unit, createdAt, updatedAt, note):
        self._student_id = student_id
        self._name = name
        self._role = role
        self._unit = unit
        self._createdAt = createdAt
        self._updatedAt = updatedAt
        self._note = note
    '''

    def getStudentId(self):
        return self._student_id
    
    def getName(self):
        return self._name
    
    def getRole(self):
        return self._role
    
    def getUnit(self):
        return self._unit
    
    def getCreatedAt(self):
        return self._createdAt
    
    def getUpdatedAt(self):
        return self._updatedAt
    
    def getNote(self):
        return self._note
    
    def dump(self):
        x = {
            "student_id": self.getStudentId(),
            "name": self.getName(),
            "role": self.getRole(),
            "unit": self.getUnit(),
            "createdAt": self.getCreatedAt(),
            "updatedAt": self.getUpdatedAt(),
            "note": self.getNote(),
        }
        return json.dump(x)
    
# Convert JSON to Python Object - https://stackabuse.com/how-to-convert-json-to-python-object/
def create_member(input):
    Member = namedtuple('Member', input.keys())
    return Member(**input)
        

class MemberModel:
    def __init__(self):
        self._file_path = 'api/models/db_member.json'

        with open(self._file_path, 'r', encoding='utf-8') as json_file:
            self.db = json.load(json_file)

        self.message = "I\'m the Member Model"

    def connection(self, database, host=None, port=None):
        if host is None or port is None:
            self.db = json.load(database)
        else:
            pass
        print("Connection to database established!")
    
    def reloadDatabase(self):

        with open(self._file_path, 'r', encoding='utf-8') as json_file:
            self.db = json.load(json_file)

    def getAllMembers(self):
        self.message = self.db.get('members')
        return self.message
    
    def getMemberById(self,memberId):
        members = self.db.get('members')
        for member in members:
            if memberId == member['student_id']:
                member_found = json.loads(json.dumps(member), object_hook=create_member)
                self.message = member_found
        return self.message
    
    def createMember(self, member):
        new_member = json.loads(member)

        with open('db_member.tmp.json','w') as db:
            l1 = self.db.get('members')
            l1.append(new_member.dump())
            db_update = {'members':l1}
            self.db.update(db_update)
            db.write(json.dumps(self.db))
        
        self.reloadDatabase()
        self.message = "User created!"
        return self.message
    
    def updateMember(self, memberId):
        self.message = "Update Member"
        return self.message
    
    def deleteMember(self, memberId):
        with open(self._file_path,'w') as db:
            l1 = self.db.get('members')
            for member in l1:
                if member['student_id'] == memberId:
                    l1.remove(member)
            db_update = {'members':l1}
            self.db.update(db_update)
            db.write(json.dumps(self.db))
        
        self.reloadDatabase()
        self.message = "Member with ID: " + memberId + " deleted!"
        return self.message