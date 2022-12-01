# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:19:59 2022

@author: ryous
"""
import os
import numpy as np
import glob
import cv2

video=cv2.VideoCapture('/Users/ryous/bunkatu.mp4')
x_size=128
y_size=160

size=(x_size,y_size)

i=0
while True:
    image,image_frame=video.read()
    #image_frame=cv2.resize(image_frame,size)
    
    if image:
        cv2.imwrite("C:/Users/ryous/Desktop/frame/IMG"+str(i)+'.jpg',image_frame)
    else:
        break
    i+=1