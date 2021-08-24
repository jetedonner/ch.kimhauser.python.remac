import subprocess
from modules.mod_interface import mod_interface

EXIT_CMD = "exit"

class mod_shellcmd(mod_interface):


    def setup_mod(self):
        print(f'Module Setup (mod_shellcmd) called successfully!')
        pass

    def run_mod(self, cmd = ""):
        answer = ""
        while True:
            cmd2send = input("$:")
            #print(f'Sending command: "{cmd2send}" to shell ...')
            try:
                args = cmd2send.split(" ")
                if args[0] == EXIT_CMD:
                    break
                answer = subprocess.check_output(cmd2send, shell=True)
                print(answer.decode("utf-8"))
            except subprocess.CalledProcessError:
                answer = f'Error sending comand "{cmd2send}" to shell!'
        return answer
