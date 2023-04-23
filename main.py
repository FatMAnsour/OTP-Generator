import os
import math
import random,sys
import smtplib
from builtins import str
from pydoc import text
from tkinter import *
from tkinter import messagebox

digits="0123456789"

window=Tk()
window.title("Tasks")
window.geometry('300x250')
window.config(bg='#F9FBE7')
frame_body = Frame(window, width=400, height=350, bg='#F9FBE7')
frame_body.grid(row=1, column=0)

mail= Entry(frame_body,bg = "light yellow")
mail.place(x=120,y=65)

otp_entry = Entry(frame_body,bg = "light yellow")
otp_entry.place(x=120,y=100)

label1=Label(frame_body,text='Email',font=('Ivy 11 bold'),height=1,bg='#F9FBE7')
label1.place(x=60,y=63)

label1=Label(frame_body,text='OTP',font=('Ivy 11 bold'),height=1,bg='#F9FBE7')
label1.place(x=60,y=100)

button1=Button(frame_body,text='Submit',command=lambda:send(mail.get()),font=('Ivy 11 bold'),height=1,bg='#F9FBE7')
button1.place(x=170,y=160)

button2=Button(frame_body,text='Verify',command=lambda:verify_otp(otp_entry.get()), font=('Ivy 11 bold'),height=1,bg='#F9FBE7')
button2.place(x=95,y=160)

#OTP Generation
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]

def send(user_email):
    email_sender = 'fatmamansour989@gmail.com'
    email_password = 'qmxeizqnihpmlunk'


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('fatmamansour989@gmail.com', 'qmxeizqnihpmlunk')

    msg = 'Your OTP Verification for app is ' + str(OTP) + ' Note..  Please enter otp within a minute , otherwise it becomes invalid'

    server.login(email_sender, email_password)
    server.sendmail(email_sender, user_email, msg)

    messagebox.showinfo("Success", "OTP sent successfully!")


def verify_otp(user_otp):
    if (user_otp) == OTP:
        messagebox.showinfo("Success", "OTP verified successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP!")




window.mainloop()