#coding:utf8
'''
Created on 2018��11��6��
reference:
https://www.jb51.net/article/135972.htm
@author: Administrator
'''
import cv2 

if __name__ == '__main__':
    vc = cv2.VideoCapture('movie/antMan.mp4') 
    print("total numer of frames:",vc.get(7))
    print("frame rate:",vc.get(5))
    print("total time:",vc.get(7)/vc.get(5)/3600,"h")
    print("width",vc.get(3),"px")
    print("height:",vc.get(4),"px")