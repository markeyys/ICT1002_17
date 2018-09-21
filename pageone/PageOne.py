import Tkinter as tk

#first page class, this is where to put all the stats (fn3-6)/graphs on the data
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="x", pady=10)
        backBtn = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("startPage"))
        NextBtn = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        checkBtn = tk.Button(self, text="Check data",
                           command=self.govt_spending) #button to output spendings on each agency
        backBtn.pack()
        NextBtn.pack()
        checkBtn.pack()

    #fn to output total spendings on each agency (**use only for data set 1**)
    def govt_spending(self):
        agencySpending=[]
        agency={} #agency to store the total counts of each agency
        agency_amt={} #agency_amt to store total spendings amount for each agency
        amount=0
        for row in self.controller.data1:
            for key, value in row.items(): #loop through each dict if agency, add a count into the agency={}
                if key=="agency":
                    # print value
                    if value not in agency:
                        agency[value]=0
                    else:
                        agency[value]+=1
            for k, v in agency.items(): #loop through each agency={} variable if matches, compile the total amt and store it in agency_amt
                if row['agency']==k:
                    amount+=float(row['awarded_amt'])
                    agency_amt[k]=amount

        print agency_amt
