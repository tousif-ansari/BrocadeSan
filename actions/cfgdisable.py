from lib.actions import BaseAction
class cfgdisable(BaseAction):
    def run(self,cfgName,ip,username,password):
        command='cfgdisable '+str(cfgName)+' -y'
        s = self.inputs(command,ip,username,password)
        return s
