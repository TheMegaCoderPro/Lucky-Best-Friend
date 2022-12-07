from tkinter import *
import random

root=Tk()

root.title("Luck Best Friend Wheel")
root.geometry("500x500")

lbf = Label(root)

list1 = ["Gray" , "Sam" , "Merrick" , "Jackson" , "Brooks" , "Manny" , "Callie" , "Paige" , "Chris" , "Ace" , "Jeremiah"]
print(list1)

def random_number():
	random_no = random.randint(0, 10)
	print(random_no)
	random_lucky_friend = list1[random_no]
	print("Your Lucky Best Friend Is: " + random_lucky_friend)
    lbf["text"] = "Your Lucky Best Friend Is: " + random_lucky_friend

btn1 = Button(root, text="Who is your Lucky Best Friend?  ", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER )

root.mainloop()