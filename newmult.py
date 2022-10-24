from threading import Thread

import cv2
import numpy as np
import os
from operator import truediv
import pandas as pd
import time
import os
from integrated import GenerateUI

def play_sound(): 
    GenerateUI()

def CV2_stuff():
    connectionCSV = pd.DataFrame()
    connectionCSV = connectionCSV.append(['Not Connected'])
    connectionCSV.to_csv('UIMetadata\Connection\connection.csv')
    print(connectionCSV.head())

    time.sleep(10)

    connectionCSV = pd.DataFrame()
    connectionCSV = connectionCSV.append(['Connected'])
    connectionCSV.to_csv('UIMetadata\Connection\connection.csv')
    print(connectionCSV.head())


    Thread(target = play_sound).start() and Thread(target = CV2_stuff).start()