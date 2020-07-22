from tkinter import *
from tkinter import filedialog
import urllib
from urllib.request import urlopen
from tkinter.messagebox import *
from sendEmail import *

root = Tk()
root.title("Email Send with Attachment")
root.geometry('750x478')
root.resizable(0,0)

photo = PhotoImage(file = "./ico.png")
root.iconphoto(False,photo)

image1= PhotoImage(file="./back.png")
label_for_image= Label(root, image=image1)
label_for_image.place(x=-2, y=-1)

EmailVar = StringVar()
SubjectVar = StringVar()

filename = None

def Dialog():
    global filename
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = 
                                            (("all files","*.*"),("jpeg files","*.jpg")))
    filename=str(filename)
    msg = f'''{filename[0:35]}
    {filename[35:]}'''
    l1.config(text=msg)

def Clear():
    EmailVar.set("")
    SubjectVar.set("")
    t1.delete('1.0',END)
    
    e1.insert(0,"Enter client email address")
    e1.bind("<FocusIn>", lambda args: e1.delete('0', 'end'))
    
    e2.insert(0,"Enter subject")
    e2.bind("<FocusIn>", lambda args: e2.delete('0', 'end'))
    
    t1.insert(END,"Enter Message...")
    t1.bind("<FocusIn>", lambda args: t1.delete('1.0',END))
    
    l1.config(text = "<<===  Please Click The Button\nTo Attach File")

def CheckInternet():
    try:
        urlopen("https://www.google.com/")
        return True
    except urllib.error.URLError as Error:
        return False

def Send():
    global filename
    if CheckInternet():
        emailVar = EmailVar.get()
        subjectVar = SubjectVar.get()
        MessageVar = t1.get('1.0',END)
        sendMail(emailVar,subjectVar,MessageVar,filename)
        showinfo("Message Sent","Your Message Has Successfully Sent...")
    else:
        showerror("Error","Your system is not connected to the internet")

Label(root,text="Email",font=('Calibri bold',25)).place(x=30,y=20)
e1 = Entry(root,font=('Calibri bold',20),bd=5,width=35,textvariable=EmailVar)
e1.place(x=220,y=20)

Label(root,text="Subject",font=('Calibri bold',25)).place(x=30,y=80)
e2 = Entry(root,font=('Calibri bold',20),bd=5,width=35,textvariable=SubjectVar)
e2.place(x=220,y=80)

Label(root,text="Message",font=("Calibri bold",25)).place(x=30,y=140)
t1=Text(root,height=4,width=35,font=('Calibri bold',20),bd=5)
t1.place(x=220,y=140)

Label(root,text="Attachment",font=("Calibri bold",25)).place(x=30,y=300)
Button(root,text="Attach File",font=('Calibri',20),bd=5,command=Dialog).place(x=220,y=300)
l1 = Label(root,text="<<===  Please Click The Button\nTo Attach File",font=("Calibri bold",15),bd=7)
l1.place(x=380,y=300)

Button(root,text="Send",font=("Calibri bold",25),bd=10,command=Send).place(x=250,y=380)
Button(root,text="Clear",font=("Calibri bold",25),bd=10,command=Clear).place(x=400,y=380)

Clear()

root.mainloop()