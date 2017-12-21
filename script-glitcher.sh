#!/bin/bash
$(for i in *.jpg; do sudo python2.7 jpglitch.py $i; done)
# (for i in ../*jpg; do sudo echo $i.png; done)
# for i in ./video_frames/*jpg; do echo $i; done