#coding:utf8
'''
Created on 2018年11月8日

@author: Administrator
'''

import os
import cv2

if __name__ == '__main__':
    
    windowSize=5
    step=1
    
    fileNameList= [[int(fileName.split(".")[0]) for fileName in fileNameList]\
                    for _,_,fileNameList in os.walk("imageDatas")]
    fileNameList=fileNameList[0]
    fileNameList=list(set(fileNameList))
    
    structuredDataList=[[[cv2.imread(os.path.join("imageDatas",str(fileNameItem)+".jpg"))\
                     for fileNameItem in fileNameList[i:i+int(windowSize/2)]+fileNameList[i+int(windowSize/2)+1:windowSize]],\
                     fileNameList[int(windowSize/2)]]\
      for i in range(len(fileNameList)-windowSize+1)]
    
    print("data shape:",structuredDataList[0][0][0].shape)