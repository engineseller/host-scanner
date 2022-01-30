#!/bash/python3

import sys
import socket
from datetime import datetime

start_time = datetime.now()

if len(sys.argv) != 7:
    print("python3 hostScanner.py -s <startip> -e <endip> -p <port>")
    sys.exit(0)


def scan(ip_address, port_number):
    if not ip_address:
        return 0

    if not port_number:
        return 0

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout in seconds
    result = tcp.connect_ex((ip_address, port_number))  # returns an error indicator => 0:success, 1:error
    tcp.close()

    if result == 0:
        return 1
    else:
        return 0


try:

    startip = sys.argv[sys.argv.index('-s') + 1]
    if not startip:
        print("Invalid startip!")
        sys.exit()

    endip = sys.argv[sys.argv.index('-e') + 1]
    if not endip:
        print("Invalid endip!")
        sys.exit()

    port = sys.argv[sys.argv.index('-p') + 1]
    if not port:
        print("Invalid port!")
        sys.exit()

    startip = list(map(int, startip.strip().split('.')))
    endip = list(map(int, endip.strip().split('.')))
    port = int(port)

    if len(startip) == 0:
        print("Invalid startip!")
        sys.exit()

    if len(endip) == 0:
        print("Invalid endip!")
        sys.exit()

    while startip != endip:
        ip = '.'.join(map(str, startip))
        if scan(ip, port):
            print(f"{ip}:{port} is live")

        startip[3] += 1
        if startip[3] % 256 == 0:
            startip[3] = 0
            if (startip[2] + 1) % 256 == 0:
                startip[2] = 0
                if (startip[1] + 1) % 256 == 0:
                    startip[1] = 0
                    if (startip[0] + 1) % 256 == 0:
                        startip[0] = 0
                    else:
                        startip[0] += 1
                else:
                    startip[1] += 1
            else:
                startip[2] += 1

except KeyboardInterrupt:
    print("\nExiting... Keyboard Error")
    sys.exit()
except IndexError:
    print("\nExiting... Index Error")
    sys.exit()

end_time = datetime.now()
total_time = end_time - start_time

print("Total time: ", total_time)
