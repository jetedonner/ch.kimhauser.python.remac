import subprocess
from apps.server.modules.mod_interface import mod_interface


class mod_interfaceRunCmd(mod_interface):

    def run_command(self, command):
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return (out + err).decode('utf-8')
