import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import asyncio
import datetime
from concurrent.futures import ThreadPoolExecutor
import time
import nest_asyncio
import random
import re
import numpy as np
import itertools
from skimage.transform import hough_circle,hough_circle_peaks
from skimage.draw import circle_perimeter
from skimage.feature import canny
from skimage import color
import cv2
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.util import img_as_ubyte
import json
import glob, os
import codecs
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from string import Template
from nltk import word_tokenize
from functools import reduce
from collections import defaultdict
import numpy as np


print('run to async functions with awaits for non-blocking processes')

async def func1(**kwargs):
    result=0
    parameters={}
    for key, value in kwargs.items():
        #print(key+":"+str(value))
        parameters[key]=value
    for i in range(parameters['parm1'],parameters['parm2']):
        result+=i
        await asyncio.sleep(0.02)
        print("func1",result)
    return result
async def func2(number, exponent):
    result=pow(number, exponent)
    for i in range(100):
        num1=pow(number+1,exponent)
        result+=num1
        print("func2",result)
        await asyncio.sleep(0.04)
    return result

          
dictParms={'parm1':200,'parm2':300}


        
if __name__ == "__main__":
    asyncio.run(main())

