from picamera import PiCamera
from os import system
from time import sleep
from datetime import datetime
camera = PiCamera()
raspistill -t 30000 -tl 2000 -o ~/Pictures/image%08d.jpg
system('convert -delay 10 -loop 0 ~/Pictures/image*.jpg ~/Pictures/animation.gif')
print('Done')
