# from modInterface import ReMacModInterface
import subprocess
import base64
from modules.mod_interface import mod_interface

OUTPUT_FILE = "sc_tmp.png"

class mod_screenshot(mod_interface):
    # def __init__(self):
    #     self.setup_mod()

    def setup_mod(self):
        print(f'Module Setup (mod_screenshot) called successfully!')
        pass

    def run_mod(self):
        self.take_screenshot()
        pass

    def run_command(self, command):
        out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return out + err

    def take_screenshot(self):
        self.run_command("screencapture -x " + OUTPUT_FILE)
        image = open(OUTPUT_FILE, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        print(f'Screenshot taken successfully!')
        return image_64_encode