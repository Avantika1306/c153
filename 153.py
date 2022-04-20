from tkinter import*
import random

root=Tk()
root.title("password generator")
root.geometry("500x500")
root.configure(background="royal blue")
label_1=Label(root)
label_1.place(relx=0.4,rely=0.6,anchor=CENTER)
array_3d=[[["1","2","3","4","5","6"],["heads","tails"],["A","B","C","D","E","F","G"]]]
def generatepass():
    random_1=random.randint(0,5)
    random_2=random.randint(0,1)
    random_3=random.randint(0,6)
    letter_1=array_3d[0][0][random_1]
    letter_2=array_3d[0][1][random_2]
    letter_3=array_3d[0][2][random_3]
    label_1["text"]=str(letter_1)+letter_2+letter_3
    
button1=Button(root,text="generate password",command=generatepass)
button1.place(relx=0.4,rely=0.5,anchor=CENTER)


root.mainloop()