# from modInterface import ReMacModInterface

class mod_hello():
    def __init__(self):
        self.setup_mod()

    def setup_mod(self):
        print(f'Module Setup (mod_hello) called successfully!')
        pass

    def run_mod(self):
        print(f'Hello Module')
        return f'HelloWorld module called!'
        pass