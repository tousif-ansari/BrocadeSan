from lib.actions import BaseAction
class alicreate(BaseAction):
    def run(self,aliName,membersList,ip,username,password):
        members = ""
        count = 0
        membersListFromSpliting=str(membersList).split(",")
        for i in membersListFromSpliting:
            count = count + 1
            if (count == 1):
                members = members + '"' + str(i) + '"'
            if (count > 1):
                members = members + ';"' + str(i) + '"'

        command='alicreate ' + str(aliName) + ', ' + str(members)
        s = self.inputs(command,ip,username,password)
        return s
