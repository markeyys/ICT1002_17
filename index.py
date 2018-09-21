
import Tkinter as tk

from Tkinter import *
from tkMessageBox import *
import tkFileDialog
from tkFileDialog import *
import csv
from start.StartPage import *
from pageone.PageOne import *
from pagetwo.PageTwo import *

#initialise main class
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #create a main frame
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)
        self.title='Anaylze Files'
        self.geometry('500x300+30+30') #set the size of the frame
        self.data1 = [] #list data 1 to store first csv file
        self.data2=[] #list data 2 to store second csv file

        #loop through each frame, if there are additional created add it in F()
        self.frames = {}
        for F in (startPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=1, column=2, sticky="nsew")
        self.show_frame("startPage")

    #raise/display a given frame based on the name given
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#start the app
if __name__=="__main__":
    app=MainApp()
    app.mainloop()
# root.destroy()
