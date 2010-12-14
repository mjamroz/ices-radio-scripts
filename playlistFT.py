#!/usr/bin/env python
# script generating random queue of mp3's from playlist.txt and add jingles (random order) after each 3 songs
# public domain

import random

playlist=[]
jinglelist=[]
jingles=9 # how many  jingles you have, 1.mp3, 2.mp3 ... jingles.mp3
jin_idx=0
shufl_idx=0
glob_idx=0
def ices_init():
	global playlist,jinglelist
	f=open("CHANGE - where is playlist.txt file").readlines()
	for line in f:
		playlist.append(line.strip())
	random.shuffle(playlist)
	for i in range(1,jingles+1):
		jinglelist.append("CHANGE /jingle/dir/path/"+str(i)+".mp3")
	random.shuffle(jinglelist)


def ices_get_next():
	global playlist, shufl_idx,jin_idx,jinglelist,glob_idx
	if(glob_idx%3==0 and glob_idx>0):# for each 3 song radio should play jingle
	   name = jinglelist[jin_idx]
	   jin_idx+=1
	   if jin_idx >=len(jinglelist):
		   jin_idx=0
		   random.shuffle(jinglelist)
	else:
	   name = playlist[shufl_idx]
  	   shufl_idx += 1
	   if shufl_idx>=len(playlist):
	   	random.shuffle(playlist)
		shufl_idx =0
	glob_idx += 1
	return name

def ices_get_metadata ():
	global glob_idx,playlist,shufl_idx
	inte=-1
	if ((glob_idx-1)%3==0 and glob_idx-1>0): # for each 3 song radio should play jingle
		result= "jingle description "
	else:

   	   if(shufl_idx==0):
		   inte = len(playlist)-1
	   else:
		   inte = shufl_idx-1
	   file=playlist[inte]
	   result = file.split("/")[-1].split(".")
	   result = ".".join(result[:len(result)-1]).replace("_"," ")
	return result


ices_init()
for i in range(20): #debug
   print ices_get_next()
   print ices_get_metadata()
