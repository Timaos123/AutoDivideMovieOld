#coding:utf8
'''
Created on 2018年11月7日

@author: Administrator
'''

import numpy as np
import matplotlib.pyplot as plt

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.utils import np_utils

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

class MyModel:
    
    def __init__(self,**kwargs):
        '''
        you can design any kinds of model in this class
        ***note:add <subtitles>***
        ==================================================
        for <CNNClassifierModel>:
        
        batch_size(default: 50):batch size
        nb_classes(default: 10):the number of classes
        nb_epoch(default: 12):the number of epoch
        nb_filters(default: 32):the number of filters
        img_rows(default: 28 ):the height of matrixes
        img_cols(default: 28):the width of matrixes
        pool_size(default: (2,2)):the size of pools
        kernel_size(default: (3,3)): the size of kernels
        ==================================================
        for <**model name**>
        parameter
        '''
        self.paraDict=kwargs
    
    def buildCNNClassifierModel(self,
                                batch_size = 50,
                                nb_classes = 10,
                                nb_epoch = 12,
                                nb_filters = 32,
                                img_rows=28,
                                img_cols =28,
                                pool_size = (2,2),
                                kernel_size = (3,3)):
        
        try:
            self.batch_size = self.paraDict['batch_size']
        except:
            self.batch_size=batch_size
            
        try:
            self.nb_classes = self.paraDict['nb_classes']
        except:
            self.nb_classes=nb_classes
            
        try:
            self.nb_epoch = self.paraDict['nb_epoch']
        except:
            self.nb_epoch=nb_epoch
            
        try:
            self.nb_filters = self.paraDict['nb_filters']
        except:
            self.nb_filters =nb_filters
            
        try:
            self.img_rows, self.img_cols = self.paraDict['img_rows'],self.paraDict['img_cols']
        except:
            self.img_rows, self.img_cols =img_rows, img_cols
            
        try:
            self.pool_size = self.paraDict['pool_size']
        except:
            self.pool_size = pool_size
            
        try:
            self.kernel_size = self.paraDict['kernel_size']
        except:
            self.kernel_size=kernel_size
            
        self.input_shape = (self.img_rows, self.img_cols,1)
            
        model = Sequential()
        
        model.add(Convolution2D(self.nb_filters, self.kernel_size[0] ,self.kernel_size[1],
                                border_mode='valid',
                                input_shape=self.input_shape))
        model.add(Activation('relu'))
        
        # 卷积层，激活函数是ReLu
        model.add(Convolution2D(self.nb_filters, self.kernel_size[0], self.kernel_size[1]))
        model.add(Activation('relu'))
        
        # 池化层，选用Maxpooling，给定pool_size，dropout比例为0.25
        model.add(MaxPooling2D(pool_size=self.pool_size))
        model.add(Dropout(0.25))
        
        # Flatten层，把多维输入进行一维化，常用在卷积层到全连接层的过渡
        model.add(Flatten())
        
        # 包含128个神经元的全连接层，激活函数为ReLu，dropout比例为0.5
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        
        # 包含10个神经元的输出层，激活函数为Softmax
        model.add(Dense(self.nb_classes))
        model.add(Activation('softmax'))
        
        model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])
        
        model.summary()
        
        self.DPmodel=model
        
        return model
    
if __name__ == '__main__':
    pass