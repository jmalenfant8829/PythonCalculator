"""
FILE          : Calculator.py
PROJECT       : Python Calculator Side Project
PROGRAMMER    : Julien Malenfant
FIRST VERSION : 24/12/2018
DESCRIPTION   : 
Defines the calculator class containing the functionality for a simple calculator
"""

class Calculator(object):
    """
       Defines functionality for a simple calculator that can store numbers and an operation,
       as well as evaluate an answer for the given numbers and operation
    """

    """
    Function    : __init__
    Description : Initialization of calculator, sets variables to default values
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def __init__(self):
        self.firstNum = '0'
        self.secondNum = ''
        self.operation = ''
        self.INFINITY = 'inf'

    """
    Function    : add
    Description : Adds two numbers together
    Parameters  :
    self        : Class reference
    num1        : First number
    num2        : Second number
    Returns     : Result of addition
    """
    def add(self, num1, num2):
        return num1 + num2
    
    """
    Function    : subtract
    Description : Subtracts one number from another
    Parameters  :
    self        : Class reference
    num1        : First number
    num2        : Second number
    Returns     : Result of subtraction
    """
    def subtract(self, num1, num2):
        return num1 - num2

    """
    Function    : multiply
    Description : Multiplies one number to another
    Parameters  :
    self        : Class reference
    num1        : First number
    num2        : Second number
    Returns     : Result of multiplication
    """
    def multiply(self, num1, num2):
        return num1 * num2

    """
    Function    : divide
    Description : Divides one number from another
    Parameters  :
    self        : Class reference
    num1        : First number
    num2        : Second number
    Returns     : Result of division
    """
    def divide(self, num1, num2):
        return num1 / num2
    
    """
    Function    : appendNum
    Description : Appends a number to the current number
    Parameters  :
    self        : Class reference
    newNum      : Number to append
    Returns     : The updated number
    """
    def appendNum(self, newNum):
        retNum = ''
        #Work with first number if operation isn't set, second if it is
        if (self.operation == ''):
             #Can't add to it if it's infinity, and can't add 0 to 0
            if (self.firstNum != self.INFINITY):
                #If there is only a 0, replace the number (to avoid displaying '08' rather than '8')
                if (self.firstNum == '0'):
                    self.firstNum = newNum
                else:
                    self.firstNum += newNum
            retNum = self.firstNum
        else:
             if (self.secondNum != self.INFINITY):
                if (self.secondNum == '0'):
                    self.secondNum = newNum
                else:
                    self.secondNum += newNum
             retNum = self.secondNum
        return retNum

    """
    Function    : clear
    Description : Resets the numbers and operations of the calculator
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def clear(self):
        #Clear all current inputs
        self.operation = ''
        self.firstNum = "0"
        self.secondNum = ''

    """
    Function    : evaluate
    Description : Evaluates the current equation if possible
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def evaluate(self):
        if (self.operation != '' and self.secondNum != ''):
            #Convert and solve equation
            answer = ''
            if (self.operation == '+'):
                answer = float(self.firstNum) + float(self.secondNum)
            elif (self.operation == '-'):
                answer = float(self.firstNum) - float(self.secondNum)
            elif (self.operation == 'x'):
                answer = float(self.firstNum) * float(self.secondNum)
            elif (self.operation == '÷'):
                #Can't divide by zero!
                if (float(self.secondNum) != 0):
                    answer = float(self.firstNum) / float(self.secondNum)
                else:
                    answer = self.INFINITY
            if (type(answer) is float):
                if (answer.is_integer()):
                    answer = int(answer)
            self.firstNum = str(answer)
            self.secondNum = ''
            self.operation = ''

    """
    Function    : appendDecimal
    Description : Appends a decimal to the current number if possible
    Parameters  :
    self        : Class reference
    Returns     : None
    """
    def appendDecimal(self):
        #Only add decimal if valid (e.g. adding decimal to 8.8 isn't valid, decimal to infinity is invalid)
        if (self.operation == '' and self.firstNum != self.INFINITY):
            if ('.' not in self.firstNum):
                self.firstNum += '.'
        else:
            if ('.' not in self.secondNum and self.secondNum != self.INFINITY):
                self.secondNum += "."