import tkinter as tk #front end package 
from tkinter import *
from GIFLoader import ImageLabel; #loads GIF
#import mp3play

#filename = "C:/PATH/TO/FILE.mp3" #file for alarm sound
#sound = mp3play.load(filename) #defines 'sound' as a variable 

root = tk.Tk()
class GenerateUI():
      # create root window
    root.title("MUSE interface")  # title of the GUI window
    #root.maxsize(1200, 2000)  # specify the max size the window can expand to
    root.config(bg="white")  # specify background color
    FontBtn=('Times', 40, 'normal') #font and size for button 
    FontCon=('Times', 30, 'normal') #font for the connection status 

    #Window Size  
    window_width = 800
    window_height = 500

    #Centers the window on the screen 
    screen_width = root.winfo_screenwidth() # get the screen dimension
    screen_height = root.winfo_screenheight() # get the screen dimension
    center_x = int(screen_width/2 - window_width / 2) # find the center point
    center_y = int(screen_height/2 - window_height / 2) # find the center point
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')  # set the position of the window to the center of the screen

    #makes row 1 bigger 
    root.rowconfigure(1, weight=3)
    root.rowconfigure(0, weight=1)

    #connection status/ gif
    response1 = Label(root, text ="Connection status: ", font=FontCon,  fg="black", bg= 'white').grid(row=0,column=0, sticky=tk.NS, padx=0, pady=0) #col moves right and left, row moves up and down 
    contectionText = Label(root, text ="Not connected", font=FontCon, fg="red", bg= 'white').grid(row=0,column=1,sticky=tk.W, padx=0, pady=2)
    lbl = ImageLabel(root)
    lbl.grid(row=1,column=0) #where gif is
    lbl.load('waveloading.gif')

    #RR and HR
    heartRate=Label(root, text="Heart Rate:", fg='black', bg='white').grid(row=2, column=0)
    respiratoryRate=Label(root, text='Respiratory Rate:', fg='black', bg='white').grid(row=2, column=1)
    
    def clicked():
        response = Label(root, text ="Alarm Stopped", fg="black", bg= 'white').grid(row=1,column=2, padx=5, pady=5)
        root.config(bg="white")
        #sound.stop()

    btn = Button(root, wraplength=140, height=7, width=12, text="Stop\nAlarm", font=FontBtn, bg='red', fg='white', command=clicked).grid(row=1, column=1, padx=0, pady=0)
        #creates stop alarm button, wraplength splits the words, height and width can be set, the font is defined before, calls the function clicked
    
    def change_color():
        current_color = btn.cget(fg)
        next_color = "green" if current_color == "black" else "black"
        btn.config(fg=next_color)
        root.after(1000, change_color)
   
    def threshold():
        #sound.play()
        root.config(bg="black")
        
    #ThresholdBtn = Button(root, text="simulate threshold is met", command=lambda:[change_color, threshold]).grid(row=3, column=0, padx=5, pady=5) 
    ThresholdBtn = Button(root, text="simulate threshold is met", command=threshold).grid(row=3, column=0, padx=5, pady=5) 

    def showConnection():
        contectionText = Label(root, text ="Connected!", fg="green", bg= 'white').grid(row=1,column=0, padx=5, pady=1)
        #play a stopped gif when its not connected 


    root.mainloop()



