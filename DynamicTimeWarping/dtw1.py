import numpy as np
import pylab
import seaborn
from collections import OrderedDict
from itertools import product
import matplotlib.font_manager as fm
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from statistics import mean
import sys
plt.style.use('ggplot')


s1 = np.array([0, 0, 1, 2, 1, 0, 1, 0, 0])
s2 = np.array([0, 1, 2, 0, 0, 0, 0, 0, 0])


ms = lambda a,b: (a - b)**2
first = lambda x: x[0]
second = lambda x: x[1]

def minVal(v1, v2, v3):
    if first(v1) <= min(first(v2), first(v3)):
        return v1, 0
    elif first(v2) <= first(v3):
        return v2, 1
    else:
        return v3, 2 

def calc_dtw(A, B):
    S = len(A)
    T = len(B)

    m = [[0 for j in range(T)] for i in range(S)]
    m[0][0] = (ms(A[0],B[0]), (-1,-1))
    for i in range(1,S):
        m[i][0] = (m[i-1][0][0] + ms(A[i], B[0]), (i-1,0))
    for j in range(1,T):
        m[0][j] = (m[0][j-1][0] + ms(A[0], B[j]), (0,j-1))

    for i in range(1,S):
        for j in range(1,T):
            minimum, index = minVal(m[i-1][j], m[i][j-1], m[i-1][j-1])
            indexes = [(i-1,j), (i,j-1), (i-1,j-1)]
            m[i][j] = (first(minimum)+ms(A[i], B[j]), indexes[index])
    return m
    
def plot_path(m, A, B):
    gs = gridspec.GridSpec(2, 2,
                       width_ratios=[1,5],
                       height_ratios=[5,1]
                       )
    ax1 = plt.subplot(gs[0])
    ax2 = plt.subplot(gs[1])
    ax4 = plt.subplot(gs[3])
    
    list_δ = [[t[0] for t in row] for row in m]
    batch = len(list_δ)
    list_δ = np.reshape(list_δ, (batch,batch))
    ax2.pcolor(list_δ, cmap=plt.cm.Blues)
    path = []
    path.append(m[-1][-1][1])
    while True:
        path.append(m[path[-1][0]][path[-1][1]][1])
        if path[-1]==(0,0):
            break
    path = np.array(path)
    ax2.plot(path[:,1], path[:,0], c="r")
    
    ax1.plot(A, range(len(A)))
    ax1.invert_xaxis()
    ax4.plot(B, c="g")
    plt.show()
    
    for line in path:
        plt.plot(line, [A[line[0]], B[line[1]]], linewidth=0.2, c="gray")
    plt.plot(A)
    plt.plot(B)
    plt.show()