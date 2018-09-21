import Tkinter as tk
from tkFileDialog import *
import csv
import os

#first page class
class startPage(tk.Frame):

    def __init__(self, parent, controller):
        self.error=False
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Import your CSV File below', font=('Arial Bold', 20))
        label.pack(side='top')
        self.controller=controller
        filename, filename2 ='','' #create string var to store the file name
        # create submit Button
        submitBtn = tk.Button(self, text="Upload",
                            command=lambda: controller.show_frame("PageOne"))
        #create file 1 button to store CSV file1
        Open_file1 = tk.Button(self, text="Open File 1",
                            command=self.readCSV1, bg='orange', fg='red')
        #create file 2 button to store CSV file2
        Open_file2 = tk.Button(self, text="Open File 2",
                            command=self.readCSV2, bg="red", fg="white")
        # note: dont use .grid when placing btn will crash
        # the higher the y the lower the btn is, the higher the x, btn is position more towards the right
        Open_file1.place(x='20', y='30', width='120', height='25')
        Open_file2.place(x='20', y='60', width='120', height='25')
        submitBtn.place(x='150', y='100', width='200', height='25')

    #fn for file1
    def readCSV1(self):
        csvfile=askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        try: #open file 1 and use DictReader to read the file
            with open(csvfile, 'r') as csv_file:
                csv_reader=csv.DictReader(csv_file)
                for row in csv_reader: #look through dictionaries and place it in data 1 list
                    self.controller.data1.append(row)
                filename=os.path.split(csvfile)[1]
                file1Label = tk.Label(self, text=filename) #create the label to store file1 name
                file1Label.place(x='150', y='30')
                print filename
        except:
            filename='No file exists'

    # fn for file 2
    def readCSV2(self):
        csvfile=askopenfilename(initialdir="/", title="Select file",
                                                filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        try: #open file 1 and use DictReader to read the file
            with open(csvfile, 'r') as csv_file:
                csv_reader=csv.DictReader(csv_file)
                for row in csv_reader: #look through dictionaries and place it in data 1 list
                    self.controller.data2.append(row)
                filename2=os.path.split(csvfile)[1]
                file2Label = tk.Label(self, text=filename2) #create the label to store file2 name
                file2Label.place(x='150', y='60')
                print filename2
        except:
            filename2='No file exists'
