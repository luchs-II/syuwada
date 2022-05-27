# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bZlph2szh22z05PMnMxUq_N_GXMBwFjI
"""

import numpy as np

def open_csv_numpy_loadtxt_skiprow(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    return data

x = open_csv_numpy_loadtxt_skiprow("./converted_pointData_datax.csv") # https://raw.githubusercontent.com/syuwadaTeam/syuwada/main/converted_pointData_datax.csv
y = open_csv_numpy_loadtxt_skiprow("./converted_pointData_datay.csv") # https://raw.githubusercontent.com/syuwadaTeam/syuwada/main/converted_pointData_datay.csv

print(x, y)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Activation
 
model = Sequential()
 
# Denseの第一引数は隠れ層のニューロン数を、
# 第二引数は入力層63個をタプル形式で指定
model.add(Dense(16, input_shape=(63,)))
model.add(Activation('relu'))
 
# 46種の分類をしたいので出力層は46を指定
model.add(Dense(46))
model.add(Activation('softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy',
             metrics=['accuracy'])
 
model.fit(x_train, y_train, epochs=50, batch_size=1, verbose=1)

loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print('Accuracy', '{:.2f}'.format(accuracy))

print(np.argmax( model.predict(x_test[5:6]) ))
print(np.argmax( y_test[5:6] ))

import pandas as pd

model.save('./model.h5')
pd.DataFrame(x).to_csv('./x.csv')

!pip3 install tensorflowjs

!tensorflowjs_converter --input_format keras model.h5 model