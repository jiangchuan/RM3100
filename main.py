#
##
#
##
#
##
#
##
#
##
#
##
#

import os
import time
from rm3100 import RM3100

DRDY = 27  # GPIO 27
SSN = 17  # GPIO 17

livoxDataDir = '/home/ubuntu/livox_data/'
if not os.path.exists(livoxDataDir):
    os.makedirs(livoxDataDir)
magDir = '/home/ubuntu/livox_data/mag/'
if not os.path.exists(magDir):
    os.makedirs(magDir)

print('Start..........')
rm3100 = RM3100(SSN, DRDY, magDir)
rm3100 = RM3100(SSN, DRDY, magDir)
millis = 0
time_before = 0
while True:
    data = rm3100.getHeading()
    if data is not None:
        millis = int(round(time.time() * 1000))
        diff = (millis - time_before)/1000
        hz = 1/diff
        print('Heading: %d, Hz: %d' % (data, hz))
        time_before = millis
