import paramiko

from st2common.runners.base_action import Action

ssh=paramiko.SSHClient()
class Connection():
    def connectionOpen(ip, username, password):

        connectionError = False
        try:
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        except:
            pass
        try:
            ssh.connect(ip, username=username, password=password, look_for_keys=False)
            return connectionError
        except:
            connectionError = True
            return connectionError

    def connectionclose(self):
        try:
            ssh.close()
        except:
            pass


class BaseAction(Action):
    def __init__(self, config=None, action_service=None):
        super(BaseAction, self).__init__(config, action_service)
        self.client = self._get_client()

    def _get_client(self):
        ip = self.config['ip']
        username = self.config['username']
        password = self.config['password']

    def inputs(self,command,ip,username,password):
        if ip==None or ip=="" or username==None or username=="" or password==None or password=="":
            k = self.client
        k = Connection()
        s = k.connectionOpen(ip, username, password)
        if (s != True):
            ssh_stdin, ssh_stdout, std_stderr = ssh.exec_command(command)
            output = ssh_stdout.readlines()
            error = std_stderr.readlines()
            if (error != []):
                try:
                    k.connectionclose()
                except:
                    pass
                return error
            else:
                try:
                    k.connectionclose()
                except:
                    pass
                return output
        else:
            return "connection Error"

