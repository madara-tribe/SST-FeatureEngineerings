#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
from DynamicTimeWarping.dtw1 import calc_dtw, plot_path
import DynamicTimeWarping.dtw
import DynamicTimeWarping.dtw_visualisation as dtwvis
import DynamicTimeWarping.dtw as dtw
import pandas as pd

def pdTo1dim(df_):
    numpy_ = df_.values
    H, W = np.shape(numpy_)
    return numpy_.reshape(H)

def plot_dtw1(d1, d2):
    # DTWの仕組み => 2つの時系列の縦軸の距離を計算
    m = calc_dtw(d1, d2)
    A=d1
    B=d2

    plot_path(m, A, B)
    print("A-B distance: ", calc_dtw(A, B)[-1][-1][0])
    


def plot_dtw2(d1, d2, window_size = 25):
    #x = np.arange(0, 20, .5)
    #s1 = np.sin(x)
    #s2 = np.sin(x - 1)
    #print(s1.shape)
    d, paths = dtw.warping_paths(d1, d2, window=window_size, psi=2)
    best_path = dtw.best_path(paths)
    dtwvis.plot_warpingpaths(d1, d2, paths, best_path)

def cal_1d_distance(d1, d2):
    #s1 = [0, 1, 1, 2, 1, 0, 1, 0, 0]
    #s2 = [0, 1, 2, 0, 0, 0, 0, 0, 0]
    distance = dtw.distance(d1, d2)
    print(distance)
    
if __name__ == '__main__':
    # data must be 1 dim just like (3000, )
    d1 = pd.read_csv('test_data1.csv', index_col=0)
    d2 = pd.read_csv('test_data2.csv', index_col=0)
    d1 = pdTo1dim(d1)
    d2 = pdTo1dim(d2)
    # dtw
    plot_dtw2(d1, d2)
    plot_dtw1(d1, d2)
    # if distance is lower, its more similar
    cal_1d_distance(d1, d2)

