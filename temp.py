import matplotlib
matplotlib.use('Agg')
import os
import cv2
from cv2 import aruco
import numpy as np
from cv2 import Rodrigues
from math import sqrt
import matplotlib.pyplot as plt
import glob
from scipy.signal import argrelextrema
import pdb
import pickle

if __name__ == '__main__':
    totaldistance = pickle.load(open('tot.p','rb'))
    tot = [x*float(10)/2.95 for x in totaldistance]
    time = pickle.load(open('time.p','rb'))
    # pdb.set_trace()
    fig,(ax) = plt.subplots(1,1)
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0,60,5))
    ax.set_yticks(np.arange(0,60,5))
    ax.plot(time,tot)
    ax.grid()
    fig.savefig('temp.png')
