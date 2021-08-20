import subprocess
from modules import mod_interface


class mod_interfaceRunCmd(mod_interface):
    def __init__(self):
        super.__init__(self)

    def run_command(self, command):
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return out + err
