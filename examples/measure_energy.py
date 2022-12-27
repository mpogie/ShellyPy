import sys
sys.path.insert(0, ".")

import ShellyPy
import time

# try connecting to the Shelly device under that ip
device = ShellyPy.Shelly("192.168.178.40")
# WILL throw an exception if the device is not reachable, gives a bad response or requires a login

device.relay(0, turn=False)
time.sleep(1)
device.relay(0, turn=True)

for j in range(120):
    stat=device.switchstatus(0)
    print(stat['aenergy'])     #print energy information
    time.sleep(1)

device.relay(0, turn=False)
