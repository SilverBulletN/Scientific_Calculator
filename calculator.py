from tkinter import *
import tkinter.messagebox
import math
import numpy as np

# Create the calculator window with a background color and title
calculator_windows = Tk()
calculator_windows.configure(bg="#202124")
calculator_windows.title("Math Calculator")

# Initialize an operator and input value string
operator = ""
input_value = StringVar()

# Create the calculator entry field
calculator_entry = Entry(
    calculator_windows, 
    font=('Helvetica', 20, 'bold'), 
    textvariable=input_value, 
    insertwidth = 7, 
    bg='#202124',
    fg='#ffffff', 
    justify='right', 
    highlightcolor='#2196f3'
    )
calculator_entry.grid(
    columnspan=7, 
    ipadx=140, ipady=10, 
    padx= 3, pady=3,  
    sticky="nsew"
    )

# Button design options    
button_design = { 
    'fg':'#ffffff', 
    'bg':'#5f6368', 
    'font':('Helvetica', 20, 'bold'), 
    'height':1, 
    'width':4
    }

# Pre-defined mathematical functions
sin = math.sin 
cos = math.cos
tan = math.tan
log = math.log
ln = math.log
e = math.exp
p = math.pi
E = '*10**'

# Function to clear the calculator
def function_delete_all():
    global operator
    operator = ""
    input_value.set("")

# Function to delete the last character entered
def function_delete_one():
    global operator
    text = operator[:-1]
    operator = text
    input_value.set(text)

# Helper function to calculate factorial
def function_factorial_help(n):
    if n==0 or n==1:
        return 1
    else:
        return n*function_factorial_help(n-1)

# Function to calculate factorial
def function_factorial():
    global operator
    result = str(function_factorial_help(int(operator)))
    operator = result
    input_value.set(result)

# Function to calculate sine
def function_sin():
    global operator
    result = str(math.sin(math.radians(int(operator))))
    operator = result
    input_value.set(result)

# Function to calculate cosine
def function_cos():
    global operator
    result = str(math.cos(math.radians(int(operator))))
    operator = result
    input_value.set(result)

# Function to calculate tangent
def function_tan():
    global operator
    result = str(math.tan(math.radians(int(operator))))
    operator = result
    input_value.set(result)

# Function to calculate cotangent
def function_cot():
    global operator
    result = str(1/math.tan(math.radians(int(operator))))
    operator = result
    input_value.set(result)

# Function to calculate square root
def function_square():
    global operator
    if int(operator)>=0:
        temp = str(eval(operator+'**(1/2)'))
        operator = temp
    else:
        temp = "ERROR"
    input_value.set(temp)

# Function to calculate percentage
def function_percent():
    global operator
    temp = str(eval(operator+'/100'))
    operator = temp
    input_value.set(temp)

def click_on(char):
     # Adds the character to the global operator string
    global operator
    operator += str(char)
    # Updates the input value
    input_value.set(operator)

def function_equal():
    # Evaluates the global operator string and updates the input value
    global operator
    try:
        if operator == "0**0":
            tkinter.messagebox.showerror("Error", "0^0 is undefined")
            operator = ""
            input_value.set("")
        else:
            temp_op = str(eval(operator))
            input_value.set(temp_op)
            operator = temp_op
    except:
        tkinter.messagebox.showerror("Error", "Invalid Input")
        operator = ""
        input_value.set("")



## Row 1
# Creates and position the 'abs' button
button_abs = Button(calculator_windows, button_design, text='abs',command=lambda:click_on('abs('))
button_abs.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")

# Creates and position the '%' button
button_percent = Button(calculator_windows, button_design, text='%',command=function_percent)
button_percent.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")

# Creates and position the 'x!' button
button_factorial = Button(calculator_windows, button_design, text='x!',command=function_factorial)
button_factorial.grid(row=1, column=2, padx=1, pady=1, sticky="nsew")

# Creates and position the '(' button
button_left_par = Button(calculator_windows, button_design, text='(',command=lambda:click_on('('))
button_left_par.grid(row=1, column=3, padx=1, pady=1, sticky="nsew")

# Creates and position the ')' button
button_right_par = Button(calculator_windows, button_design, text=')',command=lambda:click_on(')'))
button_right_par.grid(row=1, column=4, padx=1, pady=1, sticky="nsew")

# Creates and position the '←' button
button_delete_one = Button(calculator_windows, button_design,text='←', command=function_delete_one)
button_delete_one.grid(row=1, column=5, padx=1, pady=1, sticky="nsew")

# Creates and position the 'AC' button
button_delete_all = Button(calculator_windows, button_design,text='AC', command=function_delete_all)
button_delete_all.grid(row=1, column=6, padx=1, pady=1, sticky="nsew")

## Row 2
# Create and position the '%' button
button_mod = Button(calculator_windows, button_design, text='mod',command=lambda:click_on('%'))
button_mod.grid(row=2, column=0, padx=1, pady=1, sticky="nsew")

# Create and position the 'sin' button
button_sin = Button(calculator_windows, button_design, text='sin',command=function_sin)
button_sin.grid(row=2, column=1, padx=1, pady=1, sticky="nsew")

# Create and position the 'ln' button
button_ln = Button(calculator_windows, button_design, text='ln',command=lambda:click_on('ln('))
button_ln.grid(row=2, column=2, padx=1, pady=1, sticky="nsew")

# Create and position the '7' button
button_7 = Button(calculator_windows, button_design, text='7',bg='#3c4043',command=lambda:click_on('7'))
button_7.grid(row=2, column=3, padx=1, pady=1, sticky="nsew")

# Create and position the '8' button
button_8 = Button(calculator_windows, button_design, text='8',bg='#3c4043',command=lambda:click_on('8'))
button_8.grid(row=2, column=4, padx=1, pady=1, sticky="nsew")

# Create and position the '9' button
button_9 = Button(calculator_windows, button_design, text='9',bg='#3c4043',command=lambda:click_on('9'))
button_9.grid(row=2, column=5, padx=1, pady=1, sticky="nsew")

# Create and position the '/' button
button_div = Button(calculator_windows, button_design, text='/',command=lambda:click_on('/'))
button_div.grid(row=2, column=6, padx=1, pady=1, sticky="nsew")


## Row 3

# Create and position the 'pi' button
button_pi = Button(calculator_windows, button_design, text='π',command=lambda:click_on(str(math.pi)))
button_pi.grid(row=3, column=0, padx=1, pady=1, sticky="nsew")

# Create and position the 'cos' button
button_cos = Button(calculator_windows, button_design, text='cos',command=function_cos)
button_cos.grid(row=3, column=1, padx=1, pady=1, sticky="nsew")

# Create and position the logarit base 10 button
button_log = Button(calculator_windows, button_design, text='log',command=lambda:click_on('log('))
button_log.grid(row=3, column=2, padx=1, pady=1, sticky="nsew")

# Create and position the '4' button
button_4 = Button(calculator_windows, button_design, text='4',bg='#3c4043',command=lambda:click_on('4'))
button_4.grid(row=3, column=3, padx=1, pady=1, sticky="nsew")

# Create and position the '5' button
button_5 = Button(calculator_windows, button_design, text='5',bg='#3c4043',command=lambda:click_on('5'))
button_5.grid(row=3, column=4, padx=1, pady=1, sticky="nsew")

# Create and position the '6' button
button_6 = Button(calculator_windows, button_design, text='6',bg='#3c4043',command=lambda:click_on('6'))
button_6.grid(row=3, column=5, padx=1, pady=1, sticky="nsew")

# Create and position the multiplication button
button_mul = Button(calculator_windows, button_design, text='x',command=lambda:click_on('*'))
button_mul.grid(row=3, column=6, padx=1, pady=1, sticky="nsew")

## Row 4
# Create and position the euler number button
button_e = Button(calculator_windows, button_design, text='e',command=lambda:click_on(str(math.exp(1))))
button_e.grid(row=4, column=0, padx=1, pady=1, sticky="nsew")

# Create and position the tangent button
button_tan = Button(calculator_windows, button_design, text='tan',command=function_tan)
button_tan.grid(row=4, column=1, padx=1, pady=1, sticky="nsew")

# Create and position the square root button
button_square = Button(calculator_windows, button_design, text='\u00B2\u221A',command=function_square)
button_square.grid(row=4, column=2, padx=1, pady=1, sticky="nsew")

# Create and position the '1' button
button_1 = Button(calculator_windows, button_design, text='1', bg='#3c4043',command=lambda:click_on('1'))
button_1.grid(row=4, column=3, padx=1, pady=1, sticky="nsew")

# Create and position the '2' button
button_2 = Button(calculator_windows, button_design, text='2',bg='#3c4043',command=lambda:click_on('2'))
button_2.grid(row=4, column=4, padx=1, pady=1, sticky="nsew")

# Create and position the '3' button
button_3 = Button(calculator_windows, button_design, text='3',bg='#3c4043',command=lambda:click_on('3'))
button_3.grid(row=4, column=5, padx=1, pady=1, sticky="nsew")

# Create and position the subtraction button
button_sub = Button(calculator_windows, button_design, text='-',command=lambda:click_on('-'))
button_sub.grid(row=4, column=6, padx=1, pady=1, sticky="nsew")

## Row 5

# Create and position a button for the exponential function 'EXP'
button_exp = Button(calculator_windows, button_design, text='EXP', font=('sans-serif', 16, 'bold'),command=lambda:click_on(E))
button_exp.grid(row=5, column=0, padx=1, pady=1, sticky="nsew")

# Create and position the cotangent button
button_cot = Button(calculator_windows, button_design, text='cot',command=function_cot)
button_cot.grid(row=5, column=1, padx=1, pady=1, sticky="nsew")

# Create and position the nth power button
button_power = Button(calculator_windows, button_design, text='x^n',command=lambda:click_on('**'))
button_power.grid(row=5, column=2, padx=1, pady=1, sticky="nsew")

# Create and position the '0' button
button_0 = Button(calculator_windows, button_design, text='0', bg='#3c4043',command=lambda:click_on('0'))
button_0.grid(row=5, column=3, padx=1, pady=1, sticky="nsew")

# Create and position the decimal point button
button_point = Button(calculator_windows, button_design, text='.', bg='#3c4043',command=lambda:click_on('.'))
button_point.grid(row=5,  column=4, padx=1, pady=1, sticky="nsew")

# Create and position the equal button
button_equal = Button(calculator_windows, button_design, text='=', bg='#8ab4f8',command=function_equal)
button_equal.grid(row=5, column=5, padx=1, pady=1, sticky="nsew")

# Create and position the addition button
button_add = Button(calculator_windows, button_design, text='+',height=1, width=1,command=lambda:click_on('+'))
button_add.grid(row=5, column=6, padx=1, pady=1, sticky="nsew")

# Start the GUI event loop
calculator_windows.mainloop()