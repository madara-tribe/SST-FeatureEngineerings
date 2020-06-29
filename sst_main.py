#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from SST.sst import SingularSpectrumTransformation
    
def sample_data():
    x0 = 1 * np.ones(1000) + np.random.rand(1000) * 1
    x1 = 3 * np.ones(1000) + np.random.rand(1000) * 2
    x2 = 5 * np.ones(1000) + np.random.rand(1000) * 1.5
    x = np.hstack([x0, x1, x2])
    x +=  + np.random.rand(x.size)
    return x

def pdTo1dim(df_):
    numpy_ = df_.values
    H, W = np.shape(numpy_)
    return numpy_.reshape(H)

#np.random.seed(123)
def plot_data_and_score(raw_data, score):
    f, ax = plt.subplots(2,1,figsize=(20,10))
    ax[0].plot(raw_data); ax[0].set_title("raw data")
    ax[1].plot(score,"r"); ax[1].set_title("score")
    
    
def sst(x):
    # Lanczos
    score = SingularSpectrumTransformation(win_length=30, n_components=2, use_lanczos=True).score_offline(x)
    plot_data_and_score(x,score)
    
if __name__ == '__main__':  
    # data must be one dimention just like (3000,)
    d1 = pd.read_csv('test_data1.csv', index_col=0)
    d2 = pd.read_csv('test_data2.csv', index_col=0)
    d1 = pdTo1dim(d1)
    d2 = pdTo1dim(d2)
    ss = sample_data()

    sst(ss)
    sst(d1)
    sst(d2)




