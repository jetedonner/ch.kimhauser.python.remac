import clipboard
from modules.mod_interface import mod_interface
# from modInterface import ReMacModInterface

class mod_clipboard(mod_interface):
    # def __init__(self):
    #     self.setup_mod()

    def setup_mod(self):
        print(f'Module Setup (mod_clipboard) called successfully!')
        pass

    def run_mod(self):
        clipboard_content = clipboard.paste()
        print(f'Clipboard content: {clipboard_content}')
        return clipboard_content
        # pass