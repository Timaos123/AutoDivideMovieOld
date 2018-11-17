#coding:utf8
'''
Created on 2018年11月6日
reference:
https://www.jb51.net/article/135972.htm
@author: Administrator
'''
import cv2 
import os
import shutil
from PIL import Image

if __name__ == '__main__':
    
    print("clearing imageDatas ...")
    if len(list(os.walk("imageDatas")))>0:
        shutil.rmtree("imageDatas")
        os.mkdir("imageDatas")
    
    timeF = 10
    print("distinct between images is",timeF)
    
    print("loading video ...")
    vc = cv2.VideoCapture('movie/antMan.mp4')
    
    print("checking whether is open ...")
    if vc.isOpened(): #判断是否正常打开 
        rval , frame = vc.read() 
    else: 
        rval = False
      
    
    i=0    
    c=1
    while rval:
        if i<1000:
            continue
        rval, frame = vc.read() 
        if(c%timeF == 0):
            cv2.imwrite('imageDatas/'+str(i) + '.jpg',frame)
            i=i+1
            if i%200==0:
                print("the",i,"th photo")
        c = c + 1
        cv2.waitKey(1) 
        if i==1000:
            break
    vc.release()