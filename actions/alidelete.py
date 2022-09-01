from lib.actions import BaseAction
class alidelete(BaseAction):
    def run(self,aliName,ip,username,password):
        command='alidelete ' + str(aliName)
        s = self.inputs(command,ip,username,password)
        return s
