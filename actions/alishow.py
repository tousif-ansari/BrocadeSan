from lib.actions import BaseAction
class alishow(BaseAction):
    def run(self,aliName,ip,username,password):

        command='alishow ' + str(aliName)
        s = self.inputs(command,ip,username,password)
        return s
