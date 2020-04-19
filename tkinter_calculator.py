from tkinter import *
from functools import partial

#creating a tkinter window
window = Tk()
window.geometry("312x324")          #size of the window width*height
window.resizable(0,0)                # disallows window resizing
window.title("Calculator")

expression = ""
history = ""
lcounter = 0
rcounter = 0
input_text = StringVar()        # StringVar() is used to get instance of input field

def completeBrackets():                      # to make expression valid for eval if user doesn't enter all the ')' 
    global expression
    global lcounter , rcounter
    if lcounter > rcounter:
        expression = expression + ")"*(lcounter-rcounter)


def btn_click(item):                         # continuously updates the input field whenever a no is entered
    global expression, history
    global lcounter , rcounter

    if history != "" and item[0] in ["+" , "-" , "*", "/"] and expression == "":           # to continue with prev result
        expression = expression + history
        history = ""
    
    if expression != "" and expression[-1] in ["/"] and item == "0":            # for DivisionByZero Error
        input_text.set("Division By Zero Error")
        expression = expression[0:-1]
        return 0

    if item == '(':
        lcounter += 1
    elif item == ')':
        rcounter += 1

    if expression != "":
        if expression[-1] in ["+" , "-" , "*", "/"] and item in ["+" , "-" , "*", "/"]:
            expression = expression[0:-1] + str(item)           # if user wants to directly change operation
        else:
            expression = expression + str(item)
    else:
        expression = expression + str(item)

    input_text.set(expression)
 

def btn_clear():                            # clears the input field
    global expression, history
    expression = ""
    history = ""
    input_text.set(expression)

def btn_delete():                           # deletes last character
    global expression
    expression = expression[0:-1]
    input_text.set(expression)


def btn_equal():                             # calculates the expression in input field
    global expression, history
    global lcounter , rcounter
    
    completeBrackets()
    try:
        result = str(eval(expression))
        input_text.set(result)
        history = str(result)
        expression = ""
        lcounter = 0
        rcounter = 0
    except:
        input_text.set("Bad Expression")


def percentage():                            #calculates percentage
    global expression, history
    if expression == "":
        expression = expression + history
    expression = expression + "/100"
    btn_equal()

def assignPosition():       # sets most buttons in their position
    seven.grid(column = 0, row = 1)
    eight.grid(column = 1, row = 1)
    nine.grid(column = 2, row = 1)
    multiply.grid(column = 3, row = 1)
    four.grid(column = 0, row = 2)
    five.grid(column = 1, row = 2)
    six.grid(column = 2, row = 2)
    minus.grid(column = 3, row = 2)
    one.grid(column = 0, row = 3)
    two.grid(column = 1, row = 3)
    three.grid(column = 2, row = 3)
    plus.grid(column = 3, row = 3)
    zero.grid(row=4, column = 0)
    lparanthesis.grid(row=4, column = 1)
    rparanthesis.grid(row=4, column = 2)
    point.grid(row=4, column = 3)
    equal.grid(row = 4, column = 4)


#creating a frame for input field
input_frame = Frame(window, width = 312, height = 50, bd=0, highlightbackground = "black", highlightcolor = "black")
input_frame.pack(side = TOP)

# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 18, 'bold') , textvariable = input_text, width = 50, bg = "#eee", bd=0)
input_field.grid(row = 0 , column = 0)
input_field.pack(ipady = 10)    #internal padding


# creating another 'Frame for the buttons
btns_frame = Frame(window, width = 312 , height = 218, bg = "grey")
btns_frame.pack()

# first row
clear = Button(btns_frame, text="AC", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = btn_clear).grid(row = 0 , column = 0)
delete = Button(btns_frame, text="del", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = btn_delete).grid(row = 0 , column = 1)
percent = Button(btns_frame, text="%", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = percentage).grid(row = 0 , column = 2)
devide = Button(btns_frame, text="/", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = partial( btn_click, "/" )).grid(row = 0 , column = 3)

#second row
seven = Button(btns_frame, text="7", fg="black", width=10, height=3,  bd=1,bg="#eee",  cursor="hand2", command = partial( btn_click, "7" ))
eight = Button(btns_frame, text="8", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = partial( btn_click, "8" ))
nine = Button(btns_frame, text="9", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = partial( btn_click, "9" ))
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3,  bd=1,bg="#eee", cursor="hand2", command = partial( btn_click, "*" ))

# third row
four = Button(btns_frame, text="4", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "4" ))
five = Button(btns_frame, text="5", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "5" ))
six = Button(btns_frame, text="6", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "6" ))
minus = Button(btns_frame, text="-", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "-" ))


# fourth row
one = Button(btns_frame, text="1", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "1" ))
two = Button(btns_frame, text="2", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "2" ))
three = Button(btns_frame, text="3", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "3" ))
plus = Button(btns_frame, text="+", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "+" ))

#Last row frame
ze_frame = Frame(window, width = 312 , height = 54.5, bg = "grey")
ze_frame.pack()

# fifth row
zero = Button(ze_frame, text="0", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "0" ))
lparanthesis = Button(ze_frame, text="(", fg="black", width=4, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "(") )
rparanthesis = Button(ze_frame, text=")", fg="black", width=4, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, ")") )
point = Button(ze_frame, text=".", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = partial( btn_click, "." ))
equal = Button(ze_frame, text="=", fg="black", width=10, height=3,  bd=1, bg="#eee", cursor="hand2", command = btn_equal)


assignPosition()

window.mainloop()       # to close window only manually