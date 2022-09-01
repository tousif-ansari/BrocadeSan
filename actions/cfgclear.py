from lib.actions import BaseAction
class cfgclear(BaseAction):
    def run(self,cfgName,ip,username,password):

        command='cfgclear '+str(cfgName)
        s = self.inputs(command,ip,username,password)
        return s
