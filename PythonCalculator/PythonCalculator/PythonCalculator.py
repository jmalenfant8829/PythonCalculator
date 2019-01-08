"""
FILE          : PythonCalculator.py
PROJECT       : Python Calculator Side Project
PROGRAMMER    : Julien Malenfant
FIRST VERSION : 24/12/2018
DESCRIPTION   : 
Drives the calculator application
"""
from CalculatorGUI import CalculatorGUI

import tkinter
from tkinter.constants import *

def main():
    root = tkinter.Tk()
    calcGui = CalculatorGUI(root)
    root.mainloop()
    return 0

if __name__=='__main__':
    main()