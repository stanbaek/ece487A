# USB VCP example.
# This example shows how to use the USB VCP class to send an image to PC on demand.
#
# WARNING:
# This script should NOT be run from the IDE or command line, it should be saved as main.py
# Note the following commented script shows how to receive the image from the host side.
#
# #!/usr/bin/env python2.7
# import sys, serial, struct
# port = '/dev/ttyACM0'
# sp = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
#             xonxoff=False, rtscts=False, stopbits=serial.STOPBITS_ONE, timeout=None, dsrdtr=True)
# sp.setDTR(True) # dsrdtr is ignored on Windows.
# sp.write("snap")
# sp.flush()
# size = struct.unpack('<L', sp.read(4))[0]
# img = sp.read(size)
# sp.close()
#
# with open("img.jpg", "w") as f:

#     f.write(img)

import sensor, image, time, ustruct
from pyb import USB_VCP

usb = USB_VCP()

while(True):
    if not usb.any():
        continue

    msg = usb.readline().strip().decode('utf-8')

    if msg == 'cmd_gettags':
        print(msg)
    else:
        usb.send('got it')
        print(msg)

    #time.sleep_ms(10)

