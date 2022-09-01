from lib.actions import BaseAction
class zoneadd(BaseAction):
    def run(self,zoneName,membersList,ip,username,password):
        members = ""
        count = 0
        membersListFromSpliting=str(membersList).split(",")
        for i in membersListFromSpliting:
            count = count + 1
            if (count == 1):
                members = members + '"' + str(i) + '"'
            if (count > 1):
                members = members + ';"' + str(i) + '"'

        command='zoneadd '+str(zoneName)+', '+str(members)
        s = self.inputs(command,ip,username,password)
        return s
