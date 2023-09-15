from api.services.member import MemberService
class MemberController:
    def __init__(self):
        self.memberService = MemberService()
        self.message = "Hi, I'm a Member Controller"

    def getAllMembers(self):
        self.message = self.memberService.getAllMembers()
        return self.message
    
    def getMemberById(self, memberId):
        self.message = self.memberService.getMemberById(memberId)
        return self.message
    
    def createMember(self, member):
        self.message = self.memberService.createMember(member)
        return self.message
    
    def updateMember(self, memberId):
        self.message = "Update Member" # self.memberService.updateMember()
        return self.message
    
    def deleteMember(self, memberId):
        self.message = "Delete Member" # self.memberService.deleteMember()
        return self.message