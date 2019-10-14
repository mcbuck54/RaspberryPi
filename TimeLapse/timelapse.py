from picamera import PiCamera
from os import system
from time import sleep
from datetime import datetime
camera = PiCamera()
for i in range(5):
    thefilename = "~/Pictures/" + datetime.now().strftime("image%Y%m%d-%H%M%S") + ".jpg"
    print (thefilename)
    camera.capture (thefilename)
    sleep(10)
system('convert -delay 10 -loop 0 ~/Pictures/image*.jpg ~/Pictures/animation.gif')
print('Done')
