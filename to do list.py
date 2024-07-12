from tkinter import *           #for import all the default functions of tkinter library
import tkinter as tk              # tkinter library for gui 
 
from tkinter import messagebox                 # for show a messagebox in all the functions 

from PIL import ImageTk, Image                 # for import images in a program 

from datetime import datetime


# add all the functions for our task such as create_task ,delete_task,update_task and track for task 

# Function for real time and date 
def update_clock():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000,update_clock)           #update every second


# Function to create / Add a new task
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)         #condition check for insert function 
    else:
        messagebox.showwarning("Alert!!!", "please enter your task.")    #use of messagebox library for show the warning

# Function to delete a selected task 
def delete_task():
    try:
        index = listbox_tasks.curselection()[0]          #check for the index errors
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Alert!!!", "please select   your task to delete ")

# Function to update a selected task 
def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index,updated_task)
            entry_task.delete(0, tk.END)                 #for insert a new task in the place of updated task 
        else:
            messagebox.showwarning("Alert", "please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Alert!!!", "please select a task to update.")

#Function to mark done a completed task
def mark_done():
    index = listbox_tasks.curselection()
    if mark_done:
        item = listbox_tasks.get(index)
        if item.startswith("✔️"):
           listbox_tasks.itemconfig(index, mark_done )         #for configuration of the selected task for mark 
           listbox_tasks.delete(index)
           listbox_tasks.insert(END, item[1:])
        else:
            listbox_tasks.itemconfig(index)
            listbox_tasks.delete(index)
            listbox_tasks.insert(END, "✔️" + item )


# For create the main window
root = tk. Tk ()

root.geometry("700x800")            #for frame height and width

# width and height of main window 
root.minsize(200,100)

# width and height
root.maxsize(700,750)



# title for frame or task 
root.title("To-Do-List ---By ilma ")


# main or center heading for the application 
head_label = Label(root,text = "TO DO LIST",font = "monospace, 20 bold ", width = 10, bd=4, bg="purple", fg="white")
head_label.pack(side="top", fill=BOTH)          #pack method used for arrangemnt of the widgets such as buttons 


# clock block 
clock_label = tk.Label(root, font="monospace, 14 bold",width = 10,bd=3, bg="purple",fg="white")
clock_label.pack(side="top", fill=BOTH)
update_clock()

# for the setup of image background
background_image = Image.open("to do list.jpg")
background_photo = ImageTk.PhotoImage(background_image)           #use of PIL module for loadding of the image in a background 



#create a canvas widget to place the image background
canvas = tk.Canvas(root, width = background_image.width, height = background_image.height)
canvas.pack(fill = tk.BOTH, expand = tk.YES)                  #canvas is allow to you create a rectangular black area 
canvas.create_image(0,0.5, image=background_photo, anchor = tk.NW)          #anchor attribute is use to define the position of the text 


# create a frame for the to-do-list
frame_tasks = tk.Frame(root)
frame_tasks.place(relwidth = 0.8, relheight =  0.7, relx = 0.1, rely = 0.1  )


# create a listbox to display the tasks 
listbox_tasks = tk.Listbox(frame_tasks, font="Arial, 12 bold",bg="pink",fg="black")
listbox_tasks.pack(side = tk.LEFT, fill = tk.BOTH, expand = tk.YES)


# create scrollbar for the to do list display 
scrollbar_tasks = tk.Scrollbar(frame_tasks )
scrollbar_tasks.pack(side = tk.RIGHT, fill = tk.BOTH)


# link created scrollbar to the listbox 
listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command = listbox_tasks.yview)



# create an entry box to add new tasks 
entry_task= tk.Entry(root,font=("Arial, 12"),bg="skyblue",fg="black")
entry_task.place(relwidth=0.80,relheight=0.05, relx=0.1, rely=0.80)



# create button to create or add new task in the list 
button_add_task = tk.Button(root,text = "Create ", font=("Arial,12"), bg="purple",fg="white", command=add_task)
button_add_task.place(relx=0.1, rely=0.85, relwidth=0.2, relheight=0.05)

# create button to delete  task in the list 
button_delete_task = tk.Button(root,text = "Delete ", font=("Arial,12"), bg="purple",fg="white", command=delete_task)
button_delete_task.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.05)


# create button to update task in the list 
button_update_task = tk.Button(root,text = "Update ", font=("Arial,12"), bg="purple",fg="white", command=update_task)
button_update_task.place(relx=0.3, rely=0.85, relwidth=0.2, relheight=0.05)


# create button to mark as done task in the list 
button_mark_done = tk.Button(root,text = "Done ", font=("Arial,12"), bg="purple",fg="white", command=mark_done)
button_mark_done.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.05)


root.mainloop()                         #mainloop close....................