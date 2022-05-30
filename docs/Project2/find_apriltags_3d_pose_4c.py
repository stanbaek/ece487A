# AprilTags Example
#
# This example shows the power of the OpenMV Cam to detect April Tags
# on the OpenMV Cam M7. The M4 versions cannot detect April Tags.

import sensor, image, time, math
from pyb import LED
from pyb import USB_VCP

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA) # we run out of memory if the resolution is much bigger...
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)  # must turn this off to prevent image washout...
sensor.set_auto_whitebal(False)  # must turn this off to prevent image washout...
clock = time.clock()


tag_families = 0
tag_families |= image.TAG16H5 # comment out to disable this family
#tag_families |= image.TAG25H7 # comment out to disable this family
#tag_families |= image.TAG25H9 # comment out to disable this family
#tag_families |= image.TAG36H10 # comment out to disable this family
#tag_families |= image.TAG36H11 # comment out to disable this family (default family)
#tag_families |= image.ARTOOLKIT # comment out to disable this family

red_led   = LED(1)
green_led = LED(2)
blue_led  = LED(3)
ir_led    = LED(4)

red_led.on()
green_led.on()
blue_led.on()

# Note! Unlike find_qrcodes the find_apriltags method does not need lens correction on the image to work.

# What's the difference between tag families? Well, for example, the TAG16H5 family is effectively
# a 4x4 square tag. So, this means it can be seen at a longer distance than a TAG36H11 tag which
# is a 6x6 square tag. However, the lower H value (H5 versus H11) means that the false positve
# rate for the 4x4 tag is much, much, much, higher than the 6x6 tag. So, unless you have a
# reason to use the other tags families just use TAG36H11 which is the default family.

# The AprilTags library outputs the pose information for tags. This is the x/y/z translation and
# x/y/z rotation. The x/y/z rotation is in radians and can be converted to degrees. As for
# translation the units are dimensionless and you must apply a conversion function.

# f_x is the x focal length of the camera. It should be equal to the lens focal length in mm
# divided by the x sensor size in mm times the number of pixels in the image.
# The below values are for the OV7725 camera with a 2.8 mm lens.

# f_y is the y focal length of the camera. It should be equal to the lens focal length in mm
# divided by the y sensor size in mm times the number of pixels in the image.
# The below values are for the OV7725 camera with a 2.8 mm lens.

# c_x is the image x center position in pixels.
# c_y is the image y center position in pixels.

# QQVGA = 160 x 120
f_x = (2.8 / 3.984) * 160 # find_apriltags defaults to this if not set
f_y = (2.8 / 2.952) * 120 # find_apriltags defaults to this if not set
c_x = 160 * 0.5 # find_apriltags defaults to this if not set (the image.w * 0.5)
c_y = 120 * 0.5 # find_apriltags defaults to this if not set (the image.h * 0.5)


# add the following lines and provide the values
# mz is the slope for the z direction
# cz is the offset for the z direction
# mx is the slope for the x direction
# my is the slope for the y direction, and it should be the same as mx

#mz = 1
#cz = 0
#mx = 1
#my = 1

mz = -0.0196
cz = -0.0022
mx = 0.01196
my = 0.01196

usb = USB_VCP()


while(True):

    if not usb.any():
        # nothing received from the serial port
        continue

    # something has arrived at the serial port
    # read the data from the serial port.
    msg = usb.readline().strip().decode('utf-8')

    if msg == 'cmd_gettags':
        print(msg)
        img = sensor.snapshot()
        tags = img.find_apriltags(fx=f_x, fy=f_y, cx=c_x, cy=c_y, families=tag_families)

        if len(tags) != 0:
            print("%d" % len(tags), end='')

            for tag in tags:
                # img.draw_rectangle(tag.rect(), color = (255, 0, 0))
                # img.draw_cross(tag.cx(), tag.cy(), color = (0, 255, 0))
                print_args =  (tag.id(), tag.x_translation()*mx, tag.y_translation()*my, tag.z_translation()*mz + cz)
                print(",%d,%f,%f,%f" % print_args, end='')

            print() # print a new line character
        else:
            print("0")

    else:
        print('Invalid command')
