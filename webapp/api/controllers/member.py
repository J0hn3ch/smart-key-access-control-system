
class MemberController:
    def __init__(self):
        #self.memberService = MemberService()
        self.message = "Hi, I'm a Member Controller"

    def getAllMembers(self):
        self.message = "All Members" # self.memberService.getAllMembers()
        return self.message
    
    def getMemberById(self,memberId):
        self.message = "Member Id" # self.memberService.getMemberById()
        return self.message
    
    def createMember(self,memberId):
        self.message = "Creating Member" + memberId # self.memberService.createMember()
        return self.message
    
    def updateMember(self, memberId):
        self.message = "Update Member" # self.memberService.updateMember()
        return self.message
    
    def deleteMember(self, memberId):
        self.message = "Delete Member" # self.memberService.deleteMember()
        return self.message