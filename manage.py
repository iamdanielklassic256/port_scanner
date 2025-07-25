import sys
import socket
from datetime import datetime

#define a target
if len(sys.argv) == 2:
    #translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Please add a target hostname or IP Address")


#show scan info
print("="* 45)
print("Scan Target: " + target)
print("Scanning started: " + str(datetime.now))
print("=" * 45)

#Run the scan
try:
    # Scan specific ports. Adjustable but recommend the well known ports 1-1023
    for port in range(1,1023):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #Scan result
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port number {} is open".format(port))
        s.close()
#intercept the scan
except KeyboardInterrupt:
    print("\nScan halt by the user")
    sys.exit()