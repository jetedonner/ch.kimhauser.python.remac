import socket
import selectors
import traceback
import libclient

conHost = "192.168.0.49"
conPort = "6890"
sel = selectors.DefaultSelector()

class reMac_client():
    def __init__(self):
        self.setup_client()

    def setup_client(self):
        print(f'Client setup successfully!')
        pass

    def create_request(self, action, value):
        if action == "helloWorld":
            return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, value=value),
            )
        else:
            return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(action + ": " + value, encoding="utf-8"),
            )

    def start_connection(self, host, port, request):
        addr = (host, port)
        print("reMac Client - Starting connection to:", addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.settimeout(5)  # 5 seconds
        try:
            sock.connect_ex(addr)
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
            message = libclient.Message(sel, sock, addr, request)
            sel.register(sock, events, data=message)
            return True
        except socket.error as exc:
            print(f"Caught exception socket.error: {exc}")
            return False
        return False

    def start_client(self):
        try:
            host, port = conHost, int(conPort)
            action, value = "helloWorld", "SomeValue"
            request = self.create_request(action, value)
            connResult = self.start_connection(host, port, request)
            # if connResult:
            print(f"Connection to reMac Server ({conHost}:{conPort}) successfully established!")
            # return connResult
            try:
                while True:
                    events = sel.select(timeout=1)
                    for key, mask in events:
                        message = key.data
                        try:
                            message.process_events(mask)
                        except Exception:
                            print(
                                "main: error: exception for",
                                f"{message.addr}:\n{traceback.format_exc()}",
                            )
                            message.close()
                    # Check for a socket being monitored to continue.
                    if not sel.get_map():
                        break
            except KeyboardInterrupt:
                print("caught keyboard interrupt, exiting")
        except Exception:
            print(
                "ERROR: Connection to reMac Server: {conHost}:{conPort} failed!",
                f"\nException: {traceback.format_exc()}",
            )
            return False
        pass