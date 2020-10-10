# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:03:49 2019

@author: DELL-Pc
"""
#import pytube
from pytube import YouTube

yt= YouTube("https://www.youtube.com/watch?v=1I-3vJSC-Vo")
dw=yt.streams.get_by_itag(22)
dw.download("D:/")
#cprint(dir(YouTube))
#print(help(YouTube))

#print(dw)

