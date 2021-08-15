from tkinter import *
import random

root = Tk()
root.title("dice simulator")
root.geometry("500x600")

label = Label(root, font =("Helvetica" , 300 , "bold"), text = "")

def rolldice():
    dice= ["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button= Button(root, font =("Helvetica" , 25 , "bold"), text = "Roll the dice", command= rolldice)
button.pack()

root.mainloop()