#coding:utf8
'''
Created on 2018年11月7日

@author: Administrator
'''

from PIL import Image
import os
import tqdm

if __name__ == '__main__':
    i=0
    resizedWidth=256
    resizedHeight=256
    for _, _, files in os.walk("imageDatas"):
        for f in tqdm.tqdm(files):
            if i<1000:
                continue
            fp = os.path.join("imageDatas",f)
            img = Image.open(fp)
            
            print("cutting subtitles ...")
            w, h = img.size
            img=img.crop((0,0,w,7/8*h))
            
            print("resizing ...")
            img.resize((resizedWidth, resizedHeight)).save(fp, "JPEG")
            img.close