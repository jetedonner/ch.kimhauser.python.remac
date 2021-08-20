import subprocess
from modules.mod_interface import mod_interface


class mod_shellcmd(mod_interface):

    def setup_mod(self):
        print(f'Module Setup (mod_shellcmd) called successfully!')

    def run_mod(self):
        cmd2send = input("Enter shell command to send: ")
        print(f'Sending command: "{cmd2send}" to shell ...')
        try:
            output = subprocess.check_output(
                cmd2send,
                shell=True)
            print(output.decode("utf-8"))
        except subprocess.CalledProcessError:
            output = "Error sending shell command!"

        return output
