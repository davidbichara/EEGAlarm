import tkinter as tk
from tkinter import *
from GIFLoader import ImageLabel;
import pandas as pd
import time
from threading import Thread
import os
from connection import connection


root = tk.Tk()
class GenerateUI():
      # create root window
    print("UI Starting...")
    root.title("Mind Alarm")  # title of the GUI window
    root.maxsize(900, 600)  # specify the max size the window can expand to
    root.config(bg="white")  # specify background color

    ############################
    response = Label(root, text ="Connection status: ",  fg="black", bg= 'white')
    response.grid(row=0,column=0, padx=5, pady=5)
    connectionStatus = tk.StringVar()
    connectionStatus.set("Not Connected")
    connectionColor = tk.StringVar()
    connectionColor.set("red")
    connectionLabel = Label(root, textvariable =connectionStatus, fg="red", bg= 'white')
    connectionLabel.grid(row=1,column=0, padx=5, pady=1)
    ######################################
    gif = ImageLabel(root)
    gif.grid(row=3,column=0)

    gif.load('waveloading.gif')

    def clicked():
        response = Label(root, text ="Alarm Stopped", fg="black", bg= 'white')
        response.grid(row=4,column=1, padx=5, pady=5)


    response = Label(root, text ="", fg="black", bg= 'white')
    response.grid(row=4,column=1, padx=5, pady=5)
    btn = Button(root, text="Stop Alarm", command=clicked)
    btn.grid(row=3, column=1, padx=5, pady=5)

   # def showConnection():
    #    contectionText = Label(root, text ="Connected!", fg="green", bg= 'white').grid(row=1,column=0, padx=5, pady=1)
    def updateConnection(connectionStatus, connectionLabel):
        if os.path.exists('UIMetadata\Connection\connection.csv'): # arr
            connection = pd.read_csv('UIMetadata\Connection\connection.csv').iloc[0, 1]
            #print(connection.shape)
            connectionStatus.set(connection)
            color = "green" if connection == "Connected" else "red"
            connectionLabel.config(fg=color)
   
    while True:
        #time.sleep(5)
        updateConnection(connectionStatus, connectionLabel)
        root.update_idletasks()
        root.update()



