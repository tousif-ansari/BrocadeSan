from lib.actions import BaseAction
class cfgremove(BaseAction):
    def run(self,cfgName,ip,username,password):

        command='cfgremove "'+str(cfgName)
        s = self.inputs(command,ip,username,password)
        return s
