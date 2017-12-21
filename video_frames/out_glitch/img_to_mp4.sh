#!/bin/bash
NOW=$(date +"%m_%d_%Y")
ffmpeg -i output_%05d_glitched.png -c:v libx264 -vf "fps=25, format=yuv420p" $NOW.mp4