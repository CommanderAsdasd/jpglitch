INPUT_VID=$1;
FRAMEPERSEC=$2;
ffmpeg -i $INPUT_VID -r $FRAMEPERSEC output_%05d.jpg