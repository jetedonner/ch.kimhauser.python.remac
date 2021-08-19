#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback

import libclient

authorName = "JeteDonner"
appVersion = "0.0.1"
appDate = "2021-08-17"
conHost = "192.168.0.49"
conPort = "6890"

sel = selectors.DefaultSelector()


def create_request(action, value):
    if action == "search":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    elif action == "screenshot":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    elif action == "clipboard":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    elif action == "chromehist":
        return dict(
            type="text/json",
            encoding="utf-8",
            content=dict(action=action, value=value),
        )
    elif action == "webcam":
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


def start_connection(host, port, request):
    addr = (host, port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def print_client_help():
    print(f'Client script by {authorName}\nVersion: {appVersion}, {appDate}\n')
    print(f'Commands: ')
    print(f'w\t\t\tTake photo with the webcam')
    print(f'c\t\t\tGet clipboard content')
    print(f's\t\t\tGet screenshot')

def sendMessage2Server(msg4Server):
    host = "192.168.0.49"
    port = 6890
    action = msg4Server
    value = "hello"
    request = create_request(action, value)
    start_connection(host, port, request)

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


if len(sys.argv) != 5:
    print("usage:", sys.argv[0], "<host> <port> <action> <value>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
action, value = sys.argv[3], sys.argv[4]
request = create_request(action, value)
start_connection(host, port, request)

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
# finally:
#     sel.close()
print_client_help()
while True:
    # print(f'Select option to continue:')
    # c = wait_key()
    c = input("Select CLIENT option and press enter:")
    print(c)
    if c == "q":
        sys.exit(1)
        break
    elif c == "s":
        sendMessage2Server("screenshot")
        # host = "192.168.0.49"
        # port = 6890
        # action = "screenshot"
        # value = "hello"
        # request = create_request(action, value)
        # start_connection(host, port, request)
        #
        # try:
        #     while True:
        #         events = sel.select(timeout=1)
        #         for key, mask in events:
        #             message = key.data
        #             try:
        #                 message.process_events(mask)
        #             except Exception:
        #                 print(
        #                     "main: error: exception for",
        #                     f"{message.addr}:\n{traceback.format_exc()}",
        #                 )
        #                 message.close()
        #         # Check for a socket being monitored to continue.
        #         if not sel.get_map():
        #             break
        # except KeyboardInterrupt:
        #     print("caught keyboard interrupt, exiting")
    elif c == "w":
        sendMessage2Server("webcam")
        # host = "192.168.0.49"
        # port = 6890
        # action = "webcam"
        # value = "hello"
        # request = create_request(action, value)
        # start_connection(host, port, request)
        #
        # try:
        #     while True:
        #         events = sel.select(timeout=1)
        #         for key, mask in events:
        #             message = key.data
        #             try:
        #                 message.process_events(mask)
        #             except Exception:
        #                 print(
        #                     "main: error: exception for",
        #                     f"{message.addr}:\n{traceback.format_exc()}",
        #                 )
        #                 message.close()
        #         # Check for a socket being monitored to continue.
        #         if not sel.get_map():
        #             break
        # except KeyboardInterrupt:
        #     print("caught keyboard interrupt, exiting")
    elif c == "c":
        sendMessage2Server("clipboard")
    elif c == "h":
        sendMessage2Server("chromehist")
        # host = "192.168.0.49"
        # port = 6890
        # action = "clipboard"
        # value = "hello"
        # request = create_request(action, value)
        # start_connection(host, port, request)
        #
        # try:
        #     while True:
        #         events = sel.select(timeout=1)
        #         for key, mask in events:
        #             message = key.data
        #             try:
        #                 message.process_events(mask)
        #             except Exception:
        #                 print(
        #                     "main: error: exception for",
        #                     f"{message.addr}:\n{traceback.format_exc()}",
        #                 )
        #                 message.close()
        #         # Check for a socket being monitored to continue.
        #         if not sel.get_map():
        #             break
        # except KeyboardInterrupt:
        #     print("caught keyboard interrupt, exiting")
