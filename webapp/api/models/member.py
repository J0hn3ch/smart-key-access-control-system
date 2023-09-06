class MemberModel:
    def __init__(self):
        self.message = "Hi, I'm a Member Controller"

    def getAllMembers(self):
        self.message = "All Members"
        return self.message
    
    def getMemberById(self,memberId):
        self.message = "Member Id"
        return self.message
    
    def createMember(self,memberId):
        self.message = "Creating Member" + memberId
        return self.message
    
    def updateMember(self, memberId):
        self.message = "Update Member"
        return self.message
    
    def deleteMember(self, memberId):
        self.message = "Delete Member"
        return self.message
    