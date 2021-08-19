# from modInterface import ReMacModInterface
# import mod_interface
from modules.mod_interface import mod_interface

class mod_hello(mod_interface):

    def setup_mod(self):
        print(f'Module Setup (mod_hello) called successfully!')
        pass

    def run_mod(self):
        print(f'Hello Module')
        return f'HelloWorld module called!'
        pass