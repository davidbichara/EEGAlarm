from operator import truediv
import pandas as pd
import time
import os
from threading import Thread
from integrated import GenerateUI

class connection():
    b = False
    if b:
        connectionCSV = pd.read_csv('UIMetadata\Connection\connection.csv')
        print(connectionCSV.head())
    else:
        connectionCSV = pd.DataFrame()
        connectionCSV = connectionCSV.append(['Not Connected'])
        connectionCSV.to_csv('UIMetadata\Connection\connection.csv')
        print(connectionCSV.head())
        
        Thread(target = GenerateUI).start() 
        time.sleep(5)
        
        connectionCSV = pd.DataFrame()
        connectionCSV = connectionCSV.append(['Connected'])
        connectionCSV.to_csv('UIMetadata\Connection\connection.csv')
        print(connectionCSV.head())


