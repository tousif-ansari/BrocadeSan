from lib.actions import BaseAction
class zoneremove(BaseAction):
    def run(self,zoneName,ip,username,password):

        command='zonedelete '+str(zoneName)
        s = self.inputs(command,ip,username,password)
        return s
