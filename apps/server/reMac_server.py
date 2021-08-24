import socket
import selectors
import traceback
import sys
# import keyboard
from pynput import keyboard

from apps.server.libs import reMac_libserver

# conHost = "192.168.0.49"
conHost = "127.0.0.1"
conPort = "6890"

sel = selectors.DefaultSelector()


class reMac_server():
    global doExit
    doExit = False

    def __init__(self):
        self.setup_server()

    def setup_server(self):
        print(f'Server setup successfully!')

    def accept_connection(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)
        conn.setblocking(False)
        message = reMac_libserver.reMac_libserver(sel, conn, addr)
        sel.register(conn, selectors.EVENT_READ, data=message)

    def on_press(self, key):
        if key.char == None:
            return
        if key == keyboard.Key.esc or key.char == 'q':
            # Stop listener
            self.doExit = True
            # message.close()
            # sel.close()
            sys.exit(1)
            # return False
        # else:
        #     _start()

    # Collect events until released


    def start_server(self, myHost = conHost, myPort = conPort):
        host, port = myHost, int(myPort)
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        lsock.bind((host, port))
        lsock.listen()
        print("reMac Server started successfully - Listening on:", (host, port))
        lsock.setblocking(False)
        sel.register(lsock, selectors.EVENT_READ, data=None)

        # with keyboard.Listener(on_press=self.on_press) as listener:
        #     listener.join()

        try:
            while True:
                # if self.doExit:
                #     break
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



        # a = [1, 2, 3, 4]
        # print("Press Enter to continue or press Esc to exit: ")
        # while True:
        #     try:
        #         if keyboard.is_pressed('ENTER'):
        #             print("you pressed Enter, so printing the list..")
        #             print(a)
        #             break
        #         if keyboard.is_pressed('Esc'):
        #             print("\nyou pressed Esc, so exiting...")
        #             sys.exit(0)
        #     except:
        #         break