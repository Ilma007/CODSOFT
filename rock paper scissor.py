# ----------------------------------------ROCK PAPER SCISSOR GAME- bY ILMA --------------------------------#
#  all the required libraries and modules for the gamr--------------------------------------

from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk                                                          #for the impoeting of images in game 
from random import randint                     #  for the scores or numbers of the game  


# create  main window
root = Tk()

root.title("Rock Paper Scissor")

root.configure(background="green")                      #set the background of the game ................


# for the width and height.....
root.geometry("1200x700")

root.minsize(200,100)
root.maxsize(1200,700)


# main or center heading for the application 

head_label = Label(root,text = "Computer",font = "monospace, 20 bold ", width = 10, bd=4, bg="red", fg="white")
head_label.grid(row=0)          # for the name of players  

head_label = Label(root,text = "User",font = "monospace, 20 bold ", width = 10, bd=4, bg="red", fg="white")
head_label.grid(row=0,column=3) 



# icon of the game 

#  for the player...........................

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))

# for the computer............................

rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper1.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor.png"))



# insert the images 
user_label = Label(root,image=scissor_img, bg="green")
comp_label = Label(root,image=scissor_img_comp, bg="green")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=3)




# scores of the game
playerScore = Label(root,text=0,font=120,bg="red",fg="white")
computerScore = Label(root, text=0, font=120,bg="red",fg="white")
computerScore.grid(row=2, column=0)
playerScore.grid(row=2, column=3)



# message for the player
msg = Label(root, font=90,text="Results", bg="red",fg="white" )
msg.grid(row=4,column=2)



# update message
def updateMessage(x):
    msg['text'] = x



# update user score 
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)



# update computer score 
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)


# check winner 
def checkWin(player,computer):
    if player == computer:
        updateMessage("Draw Match!!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "paper":
        if computer =="scissor":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    elif player == "scissor":
        if computer =="rock":
            updateMessage("You loose!!!")
            updateCompScore()
        else:
            updateMessage("You win!!!")
            updateUserScore()
    else:
        paas



# update choices
choices = ["rock","paper","scissor"]
def updateChoice(x):



# for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


#for users 
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,compChoice)

    

# buttons of the game 
rock = Button(root,width=20, height=2,text="ROCK",font="Ariel, 15 bold ",
bg="red",fg="white",command = lambda:updateChoice("rock")).grid(row=3, column=0)
                           # for the rock button 

paper = Button(root,width=20, height=2,text="PAPER",font=50,
bg="skyblue",fg="white",command = lambda:updateChoice("paper")).grid(row=3, column=2)
                           # for the paper button

scissor = Button(root,width=20, height=2,text="SCISSOR",font=50,
bg="blue",fg="white",command = lambda:updateChoice("scissor")).grid(row=3, column=3)
                           # for the scissor button 



root.mainloop()