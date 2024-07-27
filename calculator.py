from tkinter import *                             #for import all the required libraries

                                                  # for gui interface  
import tkinter as tk


#  main window
root = tk.Tk()
root.title("calculator -----by ilma")

# for width ad height of the calculator
root.geometry("350x450+100+200")
root.resizable(False,False)
root.configure(bg="black")

equation = ""

#  fuction for show  button 
def show(value):
    global equation
    equation+=value
    label.config(text=equation)


#  function for clear button  
def clear():
    global equation
    equation = ""
    label.config(text=equation)

# function for delete button 
def delete():
    global equation 
    equation = "00"
    label.config(text=equation)


# function for  calculate button 
def calcuate():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="error"
            equation =""
    label.config(text=result)
    

#  for m the main calculation display 
label=Label(root,width=20,height=2,bg="gray",fg="black",text="00",font=("arial",30))
label.pack()


# buttons for the calculator
Button(root,text="C", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "darkorange",command=lambda: clear()).place(x=10,y=100)
Button(root,text="%", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("%")).place(x=100,y=100)
Button(root,text="/", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("/")).place(x=190,y=100)


Button(root,text="7", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("7")).place(x=10,y=170)
Button(root,text="8", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("8")).place(x=100,y=170)
Button(root,text="9", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("9")).place(x=190,y=170)
Button(root,text="*", width=3, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("*")).place(x=280,y=100)
Button(root,text="-", width=3, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("-")).place(x=280,y=170)


Button(root,text="4", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("4")).place(x=10,y=240)
Button(root,text="5", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("5")).place(x=100,y=240)
Button(root,text="6", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("6")).place(x=190,y=240)


Button(root,text="1", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("1")).place(x=10,y=310)
Button(root,text="2", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("2")).place(x=100,y=310)
Button(root,text="3", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("3")).place(x=190,y=310)
Button(root,text="+", width=3, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("+")).place(x=280,y=240)


Button(root,text="00", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: delete()).place(x=10,y=380)
Button(root,text="0", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show("0")).place(x=100,y=380)
Button(root,text=".", width=4, height=1,font=("arial",20, "bold"),bd=1, fg= "white", bg = "#2a2d36",command=lambda: show(".")).place(x=190,y=380)
Button(root,text="=", width=3, height=3,font=("arial",22, "bold"),bd=1, fg= "white", bg = "darkgreen",command=lambda: calcuate()).place(x=280,y=310)






root.mainloop()