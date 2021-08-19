import sys, getopt
import os
#import os.system

# This is a sample Python script.
authorName = "JeteDonner"
appVersion = "0.0.1"
appDate = "2021-08-17"
conHost = "192.168.0.49"
conPort = "6890"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')


def print_help():
    print(f'Client-Server python script by {authorName}\nVersion: {appVersion}, {appDate}\n')
    print(f'Usage: ')
    print(f'-help, -h\t\t\tDisplay this help text')
    print(f'-server, -s\t\tStart the server')
    print(f'-client, -c\t\tStart the server')
# Press the green button in the gutter to run the script.

def main(argv):
   # try:
   opts, args = getopt.getopt(argv,"h:s:c:")
   # except getopt.GetoptError:
   #   print_help()
   #   sys.exit(2)
   for opt, arg in opts:
      if opt == '--help':
         #print(f'test.py -i <inputfile> -o <outputfile>')
         print_help()
         sys.exit()
      elif opt == '-s':
          host = arg[0:]
          port = argv[2]

          cur_dir = os.path.abspath(".")
          print(f'{cur_dir}/app-server.py {host} {port}')
          os.system(f'{cur_dir}/app-server.py {host} {port}')
      # elif opt in ("-i", "--ifile"):
      #    inputfile = arg
      # elif opt in ("-o", "--ofile"):
      #    outputfile = arg
      else:
          print_help()
   # print(f'Input file is "', inputfile)
   # print(f'Output file is "', outputfile)

# import sys, os

def wait_key():
    ''' Wait for a key press on the console and return it. '''
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
    keyPoller = KeyPoller()

    # with KeyPoller as keyPoller:
    while True:
        # print(f'Select option to continue:')
        # c = wait_key()
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
        # c = input("Press Enter to continue...")
        # print()
        # c = keyPoller.poll()
        # if not c is None:
        #     if c == "q":
        #         sel.close()
        #         sys.exit(1)
        #         break
        #     # elif c == "w":
        #     #     try:
        #     #         while True:
        #     #             events = sel.select(timeout=1)
        #     #             for key, mask in events:
        #     #                 message = key.data
        #     #                 try:
        #     #                     message.process_events(mask)
        #     #                 except Exception:
        #     #                     print(
        #     #                         "main: error: exception for",
        #     #                         f"{message.addr}:\n{traceback.format_exc()}",
        #     #                     )
        #     #                     message.close()
        #     #             # Check for a socket being monitored to continue.
        #     #             if not sel.get_map():
        #     #                 break
        #     #     except KeyboardInterrupt:
        #     #         print("caught keyboard interrupt, exiting")
        #     #     finally:
        #     #         sel.close()
        #     print(c)

if __name__ == "__main__":
    print(f'Number of arguments:', len(sys.argv), 'arguments.')
    if len(sys.argv) == 1:
        print_help()
        enterWaitForInput(sys.argv)
    else:
        main(sys.argv[1:])

# if __name__ == '__main__':
#     print_hi('PyCharm')
#     print(f'Number of arguments:', len(sys.argv), 'arguments.')
#     print(f'Argument List:', str(sys.argv))
#     if len(sys.argv) >= 2:
#         if :


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
