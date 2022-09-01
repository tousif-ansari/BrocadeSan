from lib.actions import BaseAction
class switchshow(BaseAction):
    def run(self,ip,username,password):

        command='switchshow'
        s = self.inputs(command,ip,username,password)
        return s
