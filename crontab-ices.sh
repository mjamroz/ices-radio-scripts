#!/usr/bin/env bash

ICH="icecast files (ices.conf and playlist.txt) path" #CHANGE
MUSDIR="music directory path"	#CHANGE
# mount fs
m=`df |grep encfs |wc -l`

cd $ICH
#check if processes runs
if [ `ps x | grep -v grep | grep "ices ices.conf" |wc -l` -eq 0 ]; 
then

	find $MUSDIR/ -iname "*.mp3" > $ICH/playlist.txt

	/usr/bin/ices ices.conf  
fi
