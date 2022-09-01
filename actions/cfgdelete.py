from lib.actions import BaseAction
class cfgdelete(BaseAction):
    def run(self,cfgName,ip,username,password):

        command='cfgdelete '+str(cfgName)
        s = self.inputs(command,ip,username,password)
        return s
