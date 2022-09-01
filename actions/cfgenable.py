from lib.actions import BaseAction
class cfgenable(BaseAction):
    def run(self,cfgName,membersList,ip,username,password):
        command='cfgenable '+cfgName+' -y'
        s = self.inputs(command,ip,username,password)
        return s
