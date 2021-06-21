"""
Program: MortgageCalculator.py
Programmer: Laxmi Gurung
Purpose: To create a UI for a Mortgage Calculator using Python Tkinter package
Date: 06/15/2021
"""

from tkinter import *
from tkinter import ttk

class NepalMortgageCalculator:

    def __init__(self, root):

        root.title("Nepal Mortgage Calculator")

        # Setting up the frame of the window
        mainframe = ttk.Frame(root, padding="30 30 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)


        #label = ttk.Label(text="NepalMortgageCalculator", background='gray',  foreground="white")
        #label.grid(column=1, row=1)

        # Getting user input with Entry widgets
        self.loanAmount = StringVar()
        loanAmount_entry = ttk.Entry(mainframe, width=7, textvariable=self.loanAmount)
        loanAmount_entry.grid(column=2, row=2, sticky=(W, E))
        
        self.InterestRate = StringVar()
        InterestRate_entry = ttk.Entry(mainframe, width=7, textvariable=self.InterestRate)
        InterestRate_entry.grid(column=4, row=2, sticky=(W, E))

        self.loanTerm = StringVar()
        loanTerm_entry = ttk.Entry(mainframe, width=7, textvariable=self.loanTerm)
        loanTerm_entry.grid(column=4, row=3, sticky=(W, E))

        # Creating a button for Calculate
        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=5, sticky=W)

        # Labeling all the required elements of the calculator
        ttk.Label(mainframe, text="Loan Amount", background= 'gray', foreground= 'white').grid(column=1, row=2, sticky=W)

        ttk.Label(mainframe, text="Down Payment" , background= 'gray', foreground= 'white').grid(column=1, row=3, sticky=W)

        ttk.Label(mainframe, text="Monthly Payment" , background= 'gray', foreground= 'white').grid(column=1, row=4, sticky=W)

        ttk.Label(mainframe, text="Interest Rate" , background= 'gray', foreground= 'white').grid(column=3, row=2, sticky=W)
        
        ttk.Label(mainframe, text="Loan Term" , background= 'gray', foreground= 'white').grid(column=3, row=3, sticky=W)
        
        ttk.Label(mainframe, text="Total Payment" , background= 'gray', foreground= 'white').grid(column=3, row=4, sticky=W)
        
        # These will display the output of the calculator
        self.DownPayment = StringVar()
        ttk.Label(mainframe, textvariable=self.DownPayment).grid(column=2, row=3, sticky=(W, E))
        
        self.MonthlyPayment = StringVar()
        ttk.Label(mainframe, textvariable=self.MonthlyPayment).grid(column=2, row=4, sticky=(W, E))

        self.TotalPayment = StringVar()
        ttk.Label(mainframe, textvariable=self.TotalPayment).grid(column=4, row=4, sticky=(W, E))

        #This creates padding between the widgets
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        #this assigns the function calculate to the event of the calculate widget
        root.bind("<Return>", self.calculate)

     # calculate function performs the calculation of the calculator   
    def calculate(self, *args):
        
        # Taking the user input from the entry method.
        purchasePrice = float(self.loanAmount.get())
        annualInterestRate = float(self.InterestRate.get())
        term = float(self.loanTerm.get())

        downPayment = 0.2 * purchasePrice
        fmtdownPayment = "{:.2f}".format(downPayment)
        self.DownPayment.set(fmtdownPayment)     # It displays the result

        principal = purchasePrice - downPayment
        numberPayments = term * 12

        monthlyInterestRate = annualInterestRate /100
        monthly_payment = ((principal*(monthlyInterestRate/12))/(1-((1+(monthlyInterestRate/12))**(-numberPayments))))   
        fmtmonthlyPayment = "{:.2f}".format(monthly_payment) 
        self.MonthlyPayment.set(fmtmonthlyPayment)  # It displays the result
        
        totalInt = (numberPayments * monthly_payment)-principal
        fmttotalInt = "{:.2f}".format(totalInt)

        totalPayment = totalInt + purchasePrice
        fmttotalPayment ="{:.2f}".format(totalPayment)
        self.TotalPayment.set(fmttotalPayment)# It displays the result

                                    
root = Tk()
NepalMortgageCalculator(root)
root.mainloop()
