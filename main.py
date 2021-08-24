import sys, getopt
import os

authorName = "JeteDonner"
appVersion = "0.0.1"
appDate = "2021-08-17"
conHost = "192.168.0.49"
conPort = "6890"


def print_hi(name):
    print(f'Hi, {name}')


def print_help():
    print(f'Client-Server python script by {authorName}\nVersion: {appVersion}, {appDate}\n')
    print(f'Usage: ')
    print(f'-help, -h\t\t\tDisplay this help text')
    print(f'-server, -s\t\tStart the server')
    print(f'-client, -c\t\tStart the server')


def main(argv):
    opts, args = getopt.getopt(argv,"h:s:c:")
    for opt, arg in opts:
        if opt == '--help':
            print_help()
            sys.exit()
        elif opt == '-s':
            host = arg[0:]
            port = argv[2]
            cur_dir = os.path.abspath(".")
            print(f'{cur_dir}/app-server.py {host} {port}')
            os.system(f'{cur_dir}/app-server.py {host} {port}')
        else:
            print_help()


def wait_key():
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


def enterWaitForInput(argv):
    while True:
        c = input("Select your option and press enter:")
        print(c)
        if c == "q":
            sys.exit(1)
            break
        elif c == "c":
            print(f'Staring client ... connecting to {conHost}:{conPort}')
            cur_dir = os.path.abspath(".")
            cmd = "clipboard"
            msg = "hello"
            os.system(f'{cur_dir}/app-client.py {conHost} {conPort} {cmd} {msg}')
        elif c == "s":
            print(f'Staring server @ {conHost}:{conPort}')
            cur_dir = os.path.abspath(".")
            os.system(f'{cur_dir}/app-server.py {conHost} {conPort}')


if __name__ == "__main__":
    print(f'Number of arguments:', len(sys.argv), 'arguments.')
    if len(sys.argv) == 1:
        print_help()
        enterWaitForInput(sys.argv)
    else:
        main(sys.argv[1:])
