
from tkinter import *
import math


def click(value):
    ex = entryfield.get() 
    answer = ''
    try:
        if value == 'C':
            ex = ex[0:len(ex) - 1]  
            entryfield.delete(0, END)
            entryfield2.delete(0, END)
            entryfield.insert(0, ex)
            
            return

        elif value == 'CE':
            entryfield.delete(0, END)
            entryfield2.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  
            entryfield.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):  
            entryfield.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryfield.insert(END, value)
            
            return

        entryfield.delete(0, END)
        entryfield2.delete(0, END)
        entryfield2.insert(0, answer)
    except SyntaxError:
        pass    


root=Tk()
root.title("Scientific Calculator")
root.config(bg='#00FFFF')
root.geometry('310x548+200+100')

entryfield=Entry(root,font=('arial',30),bg='#0C090A',fg='white',bd=10,relief=SUNKEN,width=13,justify='right')
entryfield.grid(row=0,column=0,columnspan=5)
entryfield2=Entry(root,font=('arial',18),bg='#0C090A',fg='white',bd=10,relief=SUNKEN,width=22,justify='right')
entryfield2.grid(row=1,column=0,columnspan=5)


C = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="C", bg='#B87333', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#B87333',command=lambda button="C":click(button))
C.grid(row=2, column=0,pady=1,padx=1)  

CE = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="CE", bg='#B87333', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#B87333',command=lambda button="CE":click(button))
CE.grid(row=2, column=1,pady=1,padx=1)

DEG = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="deg", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="deg":click(button))
DEG.grid(row=2, column=2,pady=1,padx=1)

RAD = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="rad", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="rad":click(button))
RAD.grid(row=2, column=3,pady=1,padx=1)

SR = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="√", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="√":click(button))
SR.grid(row=2, column=4,pady=1,padx=1)







CR = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=chr(8731), bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button=chr(8731):click(button))
CR.grid(row=3, column=0,pady=1,padx=1)


XPY = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="x\u02b8", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="x\u02b8":click(button))
XPY.grid(row=3, column=1,pady=1,padx=1)


XC = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="x\u00B3", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="x\u00B3":click(button))
XC.grid(row=3, column=2,pady=1,padx=1)


XS = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="x\u00B2", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="x\u00B2":click(button))
XS.grid(row=3, column=3,pady=1,padx=1)


E = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="e", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="e":click(button))
E.grid(row=3, column=4,pady=1,padx=1)





CO = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="cosθ", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="cosθ":click(button))
CO.grid(row=4, column=0,pady=1,padx=1)


TO = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="tanθ", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="tanθ":click(button))
TO.grid(row=4, column=1,pady=1,padx=1)


SO = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="sinθ", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="sinθ":click(button))
SO.grid(row=4, column=2,pady=1,padx=1)


PIE = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="π", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="π":click(button))
PIE.grid(row=4, column=3,pady=1,padx=1)


PIE2 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="2π", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="2π":click(button))
PIE2.grid(row=4, column=4,pady=1,padx=1)








CH = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="cosh", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="cosh":click(button))
CH.grid(row=5, column=0,pady=1,padx=1)


TH = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="tanh", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="tanh":click(button))
TH.grid(row=5, column=1,pady=1,padx=1)


SH = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="sinh", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="sinh":click(button))
SH.grid(row=5, column=2,pady=1,padx=1)

BL = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="(", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="(":click(button))
BL.grid(row=5, column=3,pady=1,padx=1)


BR = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=")", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button=")":click(button))
BR.grid(row=5, column=4,pady=1,padx=1)





N7 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="7", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="7":click(button))
N7.grid(row=6, column=0,pady=1,padx=1)


N8 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="8", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="8":click(button))
N8.grid(row=6, column=1,pady=1,padx=1)


N9 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="9", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="9":click(button))
N9.grid(row=6, column=2,pady=1,padx=1)


MD = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="%", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="%":click(button))
MD.grid(row=6, column=3,pady=1,padx=1)


XF = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="x!", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="x!":click(button))
XF.grid(row=6, column=4,pady=1,padx=1)






N4 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="4", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="4":click(button))
N4.grid(row=7, column=0,pady=1,padx=1)


N5 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="5", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="5":click(button))
N5.grid(row=7, column=1,pady=1,padx=1)


N6 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="6", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="6":click(button))
N6.grid(row=7, column=2,pady=1,padx=1)


MULTI = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="*", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="*":click(button))
MULTI.grid(row=7, column=3,pady=1,padx=1)


DIV = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="/", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="/":click(button))
DIV.grid(row=7, column=4,pady=1,padx=1)







N1 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="1", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="1":click(button))
N1.grid(row=8, column=0,pady=1,padx=1)


N2 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="2", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="2":click(button))
N2.grid(row=8, column=1,pady=1,padx=1)


N3 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="3", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="3":click(button))
N3.grid(row=8, column=2,pady=1,padx=1)


ADD = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="+", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="+":click(button))
ADD.grid(row=8, column=3,pady=1,padx=1)



SUB = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="-", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="-":click(button))
SUB.grid(row=8, column=4,pady=1,padx=1)








DOT = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=".", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button=".":click(button))
DOT.grid(row=9, column=0,pady=1,padx=1)


N0 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="0", bg='#2B3327', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#2B3327',command=lambda button="0":click(button))
N0.grid(row=9, column=1,pady=1,padx=1)


LOG10 = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="log₁₀", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="log₁₀":click(button))
LOG10.grid(row=9, column=2,pady=1,padx=1)


LOG = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="ln", bg='#3B3131', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#3B3131',command=lambda button="ln":click(button))
LOG.grid(row=9, column=3,pady=1,padx=1)


EQL = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text="=", bg='#272B33', fg='white',
                    font=('arial', 12, 'bold'), activebackground='#272B33',command=lambda button="=":click(button))
EQL.grid(row=9, column=4,pady=1,padx=1)



root.mainloop()