from api.models.member import MemberModel
from api.models.member import Member

class MemberService:
    def __init__(self):
        self.memberModel = MemberModel()
        self.message = {}
    
    def getAllMembers(self):
        return self.memberModel.getAllMembers()
    
    def getMemberById(self, student_id):
        return self.memberModel.getMemberById(student_id)
    
    def createMember(self, member):
        return self.memberModel.createMember(member)