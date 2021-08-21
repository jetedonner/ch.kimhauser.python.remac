import subprocess
from modules.mod_interface import mod_interface


class mod_shellcmd(mod_interface):

    def setup_mod(self):
        print(f'Module Setup (mod_shellcmd) called successfully!')
        pass

    def run_mod(self):
        cmd2send = input("Enter shell command to send: ")
        print(f'Sending command: "{cmd2send}" to shell ...')
        try:
            decrypted = subprocess.check_output(
                cmd2send,
                shell=True)
            print(decrypted.decode("utf-8"))
        except subprocess.CalledProcessError:
            decrypted = "Error sending shell command!"

        return decrypted
