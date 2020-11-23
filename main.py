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

from rm3100 import RM3100
import time
DRDY = 27  # GPIO 27
SSN = 17  # GPIO 17

print('Start..........')


rm3100 = RM3100(SSN, DRDY)
millis = 0
time_before = 0
while True:
    data = rm3100.getHeading()
    if data != None:
        millis = int(round(time.time() * 1000))
        diff = (millis - time_before)/1000
        hz = 1/diff
        print('Heading: %d, Hz: %d' % (data, hz))
        time_before = millis
