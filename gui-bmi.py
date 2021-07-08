from tkinter import *
window=Tk()
window.title("bmi calculator")
window.geometry("400x400")

window.configure(bg="lightgreen")

username=Entry(window,text="",bd=2,width=22)
username.place(x=150,y=92)

resultframe=LabelFrame(window,text="result",bg="lightblue",font=("calibri",12))
resultframe.pack(padx=20,pady=20)
resultframe.place(x=20,y=300)
resultlabel=Label(resultframe,text="",bg="lightblue",font=("calibri",12),width=33)
resultlabel.place(x=20,y=20)
resultlabel.pack()

heightlabel=Label(window,text="enter height(cm)",fg="black",bg="lightblue",font=("calibri",12))
heightlabel.place(x=20,y=140)
heightentry=Entry(window,text="",bd=2,width=15)
heightentry.place(x=150,y=142)

weightlabel=Label(window,text="enter weight(kg)",fg="black",bg="lightblue",font=("calibri",12))
weightlabel.place(x=20,y=185)
weightentry=Entry(window,text="",bd=2,width=15)
weightentry.place(x=150,y=187)


def calculatebmi():
    weight=int(weightentry.get())
    height=int(heightentry.get())/100
    bmi=weight/(height*height)
    bmi=round(bmi,1)
    name=username.get()

    resultlabel.destroy()
    msg=""
    if bmi<=18:
        msg="you are underweight"
    elif bmi>18 and bmi<=25:
        msg="you are fit"
    elif bmi>25 and bmi<=30:
        msg="you are overweight"
    elif bmi>30:
        msg="you are obese"
    
    else:
        msg:"something went wrong! Try again"

    outputmessage=Label(resultframe,text=name+" ,your bmi is "+str(bmi)+" and "+msg,bg="lightblue",font=("calibri",12),width=42)
    outputmessage.place(x=20,y=40)
    outputmessage.pack()

calculatebutton=Button(window,text="calculate",fg="black",bg="blue",bd=4,command=calculatebmi)
calculatebutton.place(x=20,y=250)



window.mainloop()



    

         