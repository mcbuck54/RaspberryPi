raspistill -t 30000 -tl 2000 -o ~/Pictures/image%08d.jpg
convert -delay 10 -loop 0 ~/Pictures/image*.jpg ~/Pictures/animation.gif
