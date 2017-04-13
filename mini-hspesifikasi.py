import numpy as np
import cv2
import matplotlib

def hspesifikasi2(Hx,Hz):
    lookup = [None] * 8
    for i in range(0,8):
        tmp = 10
        j = -1
        for k in range(0,8):
            if(tmp>(abs(Hx[i]-Hz[k]))):
                j=k
                tmp=abs(Hx[i]-Hz[k])
        lookup[i]=j
        #print i,lookup2[i]

    return lookup

Hz=[0,0,0,0.15,0.35,0.65,0.85,1]
Hx=[0.19,0.44,0.65,0.81,0.89,0.95,0.98,1]
result=hspesifikasi2(Hx,Hz)
#print coba