"""
FILE          : CAlculatorGUI.py
PROJECT       : Python Calculator Side Project
PROGRAMMER    : Julien Malenfant
FIRST VERSION : 24/12/2018
DESCRIPTION   : 
Defines the CalculatorGUI class which is a GUI for a simple calculator
"""

import tkinter
from tkinter.constants import *
from Calculator import Calculator

class CalculatorGUI(object):
    """
       Defines a GUI for a simple calculator
       Features numbered buttons and operational buttons, as well as a display for the numbers/answers
    """
    
    """
    Function    : __init__
    Description : Initialization of calculator GUI which creates a calculator with elements and events
    Parameters  :
    self        : Class reference
    master      : Reference to master tkinter GUI
    Returns     : None
    """
    def __init__(self, master):
        self.calc = Calculator()
        self.master = master
        master.title("Calculator")
        master.resizable(width=False, height=False)
        #Create calculator display
        self.txtDisplay = tkinter.Text(master, state='disabled', width=30, height=3)
        self.txtDisplay.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

        #Create calculator buttons
        self.btnClear = tkinter.Button(master, text="A/C", width=30, height=3, command=self.clearClick)
        self.btnClear.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        self.btn7 = tkinter.Button(master, text="7", width=10, height=3, command=lambda: self.numClick('7'))
        self.btn7.grid(row=2, column=0, padx=5, pady=5)

        self.btn8 = tkinter.Button(master, text="8", width=10, height=3, command=lambda: self.numClick('8'))
        self.btn8.grid(row=2, column=1, padx=5, pady=5)

        self.btn9 = tkinter.Button(master, text="9", width=10, height=3, command=lambda: self.numClick('9'))
        self.btn9.grid(row=2, column=2, padx=5, pady=5)

        self.btn4 = tkinter.Button(master, text="4", width=10, height=3, command=lambda: self.numClick('4'))
        self.btn4.grid(row=3, column=0, padx=5, pady=5)

        self.btn5 = tkinter.Button(master, text="5", width=10, height=3, command=lambda: self.numClick('5'))
        self.btn5.grid(row=3, column=1, padx=5, pady=5)

        self.btn6 = tkinter.Button(master, text="6", width=10, height=3, command=lambda: self.numClick('6'))
        self.btn6.grid(row=3, column=2, padx=5, pady=5)

        self.btn1 = tkinter.Button(master, text="1", width=10, height=3, command=lambda: self.numClick('1'))
        self.btn1.grid(row=4, column=0, padx=5, pady=5)

        self.btn2 = tkinter.Button(master, text="2", width=10, height=3, command=lambda: self.numClick('2'))
        self.btn2.grid(row=4, column=1, padx=5, pady=5)

        self.btn3 = tkinter.Button(master, text="3", width=10, height=3, command=lambda: self.numClick('3'))
        self.btn3.grid(row=4, column=2, padx=5, pady=5)

        self.btn0 = tkinter.Button(master, text="0", width=10, height=3, command=lambda: self.numClick('0'))
        self.btn0.grid(row=5, column=0, padx=5, pady=5)

        self.btnDecimal = tkinter.Button(master, text='.', width=10, height=3, command=self.decimalClick)
        self.btnDecimal.grid(row=5, column=1, padx=5, pady=5)

        self.btnEquals = tkinter.Button(master, text="=", width=10, height=3, command=self.equalsClick)
        self.btnEquals.grid(row=5, column=2, padx=5, pady=5)

        self.btnDivide = tkinter.Button(master, text='÷', width=10, height=3, command=lambda: self.operationClick('÷'))
        self.btnDivide.grid(row=2, column=3, padx=5, pady=5)

        self.btnMultiply = tkinter.Button(master, text='x', width=10, height=3, command=lambda: self.operationClick('x'))
        self.btnMultiply.grid(row=3, column=3, padx=5, pady=5)

        self.btnSubtract = tkinter.Button(master, text='-', width=10, height=3, command=lambda: self.operationClick('-'))
        self.btnSubtract.grid(row=4, column=3, padx=5, pady=5)

        self.btnPlus = tkinter.Button(master, text='+', width=10, height=3, command=lambda: self.operationClick('+'))
        self.btnPlus.grid(row=5, column=3, padx=5, pady=5)

        #Start by displaying the first number
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        self.txtDisplay.insert(INSERT, self.calc.firstNum)
        self.txtDisplay.configure(state="disable")

    """
    Function    : numClick
    Description : Number button click event which adds the selected number to the current number selection
    Parameters  :
    self        : Class reference
    num         : Number to add
    Returns     : None
    """
    def numClick(self, num):
        #Attempt to append the number
        newFirstNum = self.calc.appendNum(num)
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        self.txtDisplay.insert(INSERT, newFirstNum)
        self.txtDisplay.configure(state="disable")
        print("first num: " + str(self.calc.firstNum))
        print("second num: " + str(self.calc.secondNum))
        
    """
    Function    : clearClick
    Description : Clear button click event which clears out the current equation in the calculator
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def clearClick(self):
        self.calc.clear()
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        self.txtDisplay.insert(INSERT, self.calc.firstNum)
        self.txtDisplay.configure(state="disable")
        print("clear click")
    
    """
    Function    : decimalClick
    Description : Decimal button click event which attempts to add a decimal to the current number
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def decimalClick(self):
        #Add decimal and update display
        self.calc.appendDecimal()
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        #Display the correct updated number
        if (self.calc.operation == ''):
            self.txtDisplay.insert(INSERT, self.calc.firstNum)
            
        else:
            self.txtDisplay.insert(INSERT, self.calc.secondNum)

        self.txtDisplay.configure(state="disable")
        print("decimal click")
        
    """
    Function    : operationClick
    Description : Operation button click event which evaluates the current function if possible,
    and adds the clicked operation
    Parameters  :
    self        : Class reference
    op          : String representing the clicked operation
    Returns     : None
    """
    def operationClick(self, op):
        #Evaluate current equation
        self.calc.evaluate()
        #Report answer to screen
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        self.txtDisplay.insert(INSERT, self.calc.firstNum)
        self.txtDisplay.configure(state="disable")
        # Enter new operation
        if (self.calc.firstNum != ""):
            self.calc.operation = op
        print(self.calc.operation)
       
    """
    Function    : equalsClick
    Description : Equal button click event which evaluates the current function
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def equalsClick(self):
        #Evaluate current equation
        self.calc.evaluate()
        #Report answer to screen
        self.txtDisplay.configure(state="normal")
        self.txtDisplay.delete('1.0', END)
        self.txtDisplay.insert(INSERT, self.calc.firstNum)
        self.txtDisplay.configure(state="disable")
        print("equals click")