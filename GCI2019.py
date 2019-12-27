#GCI 2019
#Code for Mathematics game
import tkinter
import tkinter.ttk as tk

Key=["D","A","B","C","B","C","B","C","D","B"]
Points=[5,5,7,5,10,5,7,5,5,10]

def msg_sub1(x):
    def next_():
        top.destroy()
        top1.destroy()
        x()
    top=tkinter.Toplevel()
    top.geometry("250x100+120+120")
    top.title("Success!")
    label=tkinter.Label(top,text="Good job!")
    label.pack()
    b=tkinter.Button(top,text="Ok",command=next_)
    b.pack()
def msg_sub2(x):
    def next_():
        top.destroy()
        top1.destroy()
        x()
    top=tkinter.Toplevel()
    top.geometry("250x100+120+120")
    top.title("Oops")
    label=tkinter.Label(top,text="Better Luck Next Time!")
    label.pack()
    b=tkinter.Button(top,text="Ok",command=next_)
    b.pack()
def msg_sub11(x):
    def next_():
        top.destroy()
        window2.destroy()
        x()
    top=tkinter.Toplevel()
    top.geometry("250x100+120+120")
    top.title("Success!")
    label=tkinter.Label(top,text="Good job!")
    label.pack()
    b=tkinter.Button(top,text="Ok",command=next_)
    b.pack()
def msg_sub22(x):
    def next_():
        top.destroy()
        window2.destroy()
        x()
    top=tkinter.Toplevel()
    top.geometry("250x100+120+120")
    top.title("Oops")
    label=tkinter.Label(top,text="Better Luck Next Time!")
    label.pack()
    b=tkinter.Button(top,text="Ok",command=next_)
    b.pack()

def Result():
    top1=tkinter.Tk()
    window1.destroy()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    top1.title("Result")
    label1 = tkinter.Label(top1, text="RESULTS",font=("Arial",45,"underline"),bg="papaya whip")
    label1.pack()
    for i in D:
        label=tkinter.Label(top1,text="%s:%s"%(i,D[i]),bg="papaya whip",font=("Helvetica",30))
        label.pack()
def Ques10():
    def check10():
        p=answer10.get()
        if p[1].upper()==Key[9]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[9]
            else:
                temp=D[p[0].upper()]
                temp+=Points[9]
                D[p[0].upper()]=temp
            msg_sub1(Result)
        else:
            msg_sub2(Result)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q10=tkinter.Label(top1,text="Q10) If the number X78Y is divisible by 55 the value of X and Y are:", bg="papaya whip",font=("Helvetica",30))
    Q10.pack()
    A10=tkinter.Label(top1,text="A)1,0  B)4,5  C)6,5  D)None of these",bg="papaya whip",font=("Helvetica",25))
    A10.pack()
    answer10=tkinter.Entry(top1)
    answer10.pack()
    but5=tkinter.Button(top1,text="Submit",command=check10)
    but5.pack()
def Ques9():
    def check9():
        p=answer9.get()
        if p[1].upper()==Key[8]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[8]
            else:
                temp=D[p[0].upper()]
                temp+=Points[8]
                D[p[0].upper()]=temp
            msg_sub1(Ques10)
        else:
            msg_sub2(Ques10)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q9=tkinter.Label(top1,text="Q9) What is the remainder of 21 divided by 7?", bg="papaya whip",font=("Helvetica",30))
    Q9.pack()
    A9=tkinter.Label(top1,text="A)1  B)21  C)7  D)None of these",bg="papaya whip",font=("Helvetica",25))
    A9.pack()
    answer9=tkinter.Entry(top1)
    answer9.pack()
    but5=tkinter.Button(top1,text="Submit",command=check9)
    but5.pack()
def Ques8():
    def check8():
        p=answer8.get()
        if p[1].upper()==Key[7]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[7]
            else:
                temp=D[p[0].upper()]
                temp+=Points[7]
                D[p[0].upper()]=temp
            msg_sub1(Ques9)
        else:
            msg_sub2(Ques9)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q8=tkinter.Label(top1,text="Q8) What is the sum of one digit prime numbers?", bg="papaya whip",font=("Helvetica",30))
    Q8.pack()
    A8=tkinter.Label(top1,text="A)11  B)15  C)17  D)21",bg="papaya whip",font=("Helvetica",25))
    A8.pack()
    answer8=tkinter.Entry(top1)
    answer8.pack()
    but5=tkinter.Button(top1,text="Submit",command=check8)
    but5.pack()
def Ques7():
    def check7():
        p=answer7.get()
        if p[1].upper()==Key[6]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[6]
            else:
                temp=D[p[0].upper()]
                temp+=Points[6]
                D[p[0].upper()]=temp
            msg_sub1(Ques8)
        else:
            msg_sub2(Ques8)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q7=tkinter.Label(top1,text="Q7) How many factors are there in 71?", bg="papaya whip",font=("Helvetica",30))
    Q7.pack()
    A7=tkinter.Label(top1,text="A)1  B)2  C)3  D)None of these",bg="papaya whip",font=("Helvetica",25))
    A7.pack()
    answer7=tkinter.Entry(top1)
    answer7.pack()
    but5=tkinter.Button(top1,text="Submit",command=check7)
    but5.pack()
def Ques6():
    def check6():
        p=answer6.get()
        if p[1].upper()==Key[5]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[5]
            else:
                temp=D[p[0].upper()]
                temp+=Points[5]
                D[p[0].upper()]=temp
            msg_sub1(Ques7)
        else:
            msg_sub2(Ques7)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q6=tkinter.Label(top1,text="Q6) How many diagonals are there in a quadrilateral?", bg="papaya whip",font=("Helvetica",30))
    Q6.pack()
    A6=tkinter.Label(top1,text="A)1  B)4  C)2  D)3",bg="papaya whip",font=("Helvetica",25))
    A6.pack()
    answer6=tkinter.Entry(top1)
    answer6.pack()
    but5=tkinter.Button(top1,text="Submit",command=check6)
    but5.pack()
def Ques5():
    def check5():
        p=answer5.get()
        if p[1].upper()==Key[4]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[4]
            else:
                temp=D[p[0].upper()]
                temp+=Points[4]
                D[p[0].upper()]=temp
            msg_sub1(Ques6)
        else:
            msg_sub2(Ques6)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q5=tkinter.Label(top1,text="Q5) 45% of 640 + 64% of 450 =__% of 1440\nFill in the blank", bg="papaya whip",font=("Helvetica",30))
    Q5.pack()
    A5=tkinter.Label(top1,text="A)54  B)40  C)45  D)50",bg="papaya whip",font=("Helvetica",25))
    A5.pack()
    answer5=tkinter.Entry(top1)
    answer5.pack()
    but5=tkinter.Button(top1,text="Submit",command=check5)
    but5.pack()
def Ques4():
    def check4():
        p=answer4.get()
        if p[1].upper()==Key[3]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[3]
            else:
                temp=D[p[0].upper()]
                temp+=Points[3]
                D[p[0].upper()]=temp
            msg_sub1(Ques5)
        else:
            msg_sub2(Ques5)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q4=tkinter.Label(top1,text="Q4) In a Century, how many months are there?", bg="papaya whip",font=("Helvetica",30))
    Q4.pack()
    A4=tkinter.Label(top1,text="A)12  B)120  C)1200  D)12000",bg="papaya whip",font=("Helvetica",25))
    A4.pack()
    answer4=tkinter.Entry(top1)
    answer4.pack()
    but5=tkinter.Button(top1,text="Submit",command=check4)
    but5.pack()
def Ques3():
    def check3():
        p=answer3.get()
        if p[1].upper()==Key[2]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[2]
            else:
                temp=D[p[0].upper()]
                temp+=Points[2]
                D[p[0].upper()]=temp
            msg_sub1(Ques4)
        else:
            msg_sub2(Ques4)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q3=tkinter.Label(top1,text="Q3) Which of the following gives 240 when added to its own square:", bg="papaya whip",font=("Helvetica",30))
    Q3.pack()
    A3=tkinter.Label(top1,text="A)14  B)15  C)17  D)16",bg="papaya whip",font=("Helvetica",25))
    A3.pack()
    answer3=tkinter.Entry(top1)
    answer3.pack()
    but5=tkinter.Button(top1,text="Submit",command=check3)
    but5.pack()
def Ques2():
    def check2():
        p=answer2.get()
        if p[1].upper()==Key[1]:
            if D[p[0].upper()]=="Nil":
                D[p[0].upper()]=Points[1]
            else:
                temp=D[p[0].upper()]
                temp+=Points[1]
                D[p[0].upper()]=temp
            msg_sub1(Ques3)
        else:
            msg_sub2(Ques3)
    global top1
    top1=tkinter.Toplevel()
    top1.geometry("900x500+120+120")
    top1.configure(bg="papaya whip")
    
    Q2=tkinter.Label(top1,text="Q2) Cube root of 1331 is...", bg="papaya whip",font=("Helvetica",30))
    Q2.pack()
    A2=tkinter.Label(top1,text="A)11  B)12  C)13  D)14",bg="papaya whip",font=("Helvetica",25))
    A2.pack()
    answer2=tkinter.Entry(top1)
    answer2.pack()
    but5=tkinter.Button(top1,text="Submit",command=check2)
    but5.pack()

def open_window():
    def game():
        def check1():
            p=answer1.get()
            if p[1].upper()==Key[0]:
                if D[p[0].upper()]=="Nil":
                    D[p[0].upper()]=Points[0]
                else:
                    temp=D[p[0].upper()]
                    temp+=Points[0]
                    D[p[0].upper()]=temp
                msg_sub11(Ques2)
            else:
                msg_sub22(Ques2)
        count_grp=int(input1.get())
        top.destroy()
        global window2
        window2=tkinter.Tk()
        window2.geometry("900x500+120+120")
        window2.configure(bg="papaya whip")
        window2.title("The Game")
        
        L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        global D
        D={}
        for i in range(count_grp):
            D[L[i]]="Nil"
            
        Q1=tkinter.Label(window2,text="Q1) 50x + 17 = 33x + 34 \n Find x", bg="papaya whip",font=("Helvetica",30))
        Q1.pack()
        A1=tkinter.Label(window2,text="A)x=2  B)x=-1  C)x=-2  D)x=1",bg="papaya whip",font=("Helvetica",25))
        A1.pack()
        answer1=tkinter.Entry(window2)
        answer1.pack()
        but4=tkinter.Button(window2,text="Submit",command=check1)
        but4.pack()
       
        window2.mainloop()

    top=tkinter.Toplevel()
    top.geometry("800x300+120+120")
    top.configure(bg="papaya whip")
    but=tk.Button(top,text="close",command=top.destroy)
    but.pack()
    
    label3=tkinter.Label(top,text="Enter number of groups:(Maximum-26) ",bg="Papaya whip")
    label3.pack()
    input1=tkinter.Entry(top)
    input1.pack()
    but3=tkinter.Button(top,text="Continue!",command=game)
    but3.pack()

window1=tkinter.Tk()
window1.geometry("800x300+120+120")
window1.configure(bg="pale turquoise")
window1.title("Mathematics Game")

labelframe = tkinter.LabelFrame(window1,bg="pale turquoise")
labelframe.pack(fill="x",expand="no")
label1 = tkinter.Label(labelframe, text="Mathematics Game",font=("Arial",45,"underline"),bg="pale turquoise")
label1.pack()

frame2=tkinter.Frame(window1,bd=10,bg="pale turquoise")
frame2.pack(fill="both",expand="yes")


label2=tkinter.Label(frame2,text="Are You Ready To Begin The Fun Mathematics Game?",font=("Helvetica",30),bg="pale turquoise")
label2.pack()

lab=tkinter.Label(frame2,bg="pale turquoise")
lab.pack()

but1=tk.Button(frame2,text="Yes!!!",command=open_window)
but1.pack(ipadx=25,ipady=25)

window1.mainloop()