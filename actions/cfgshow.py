from lib.actions import BaseAction
class cfgshow(BaseAction):
    def run(self,cfgName,ip,username,password):

        command='cfgshow '+str(cfgName)
        s = self.inputs(command,ip,username,password)
        return s
