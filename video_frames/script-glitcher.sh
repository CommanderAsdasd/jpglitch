#!/bin/bash
$(for i in *.jpg; do sudo python2.7 ../jpglitch.py -s 50 $i; done)
# (for i in ../*jpg; do sudo echo $i.png; done)
# for i in ./video_frames/*jpg; do echo $i; doneå