#-----------Solve The Quadratic Equatin-----------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def root():
    try:
        a = float(e1.get())
        b = float(e2.get())
        c = float(e3.get())
        delta = (b*b) - (4*a*c)
        
        if delta > 0:
            x1 = (-b + delta**.5) / (2*a)
            x2 = (-b - delta**.5) / (2*a)
            label4.config(text=f"X1 = {x1:.2f}  &  X2 = {x2:.2f}", fg="blue")
        elif delta == 0:
            x = -b / (a*2)
            label4.config(text=f"X = {x:.2f}", fg="yellow")
        else:
            label4.config(text="Bedone Rishe (delta < 0)", fg="red")
            
    except ValueError:
        messagebox.showerror("Error", "Fill in the blanks or don't click submit")
        
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    label4.config(text="")
    
# main window
window = Tk()
window.title("Project")
window.configure(bg="pink")
window.geometry("520x470")

#First Frame
frame1 = Frame(window, height=50, highlightbackground="black", highlightthickness=2)
frame1.grid(padx=10, pady=10)
l0 = Label(frame1, text="Solve The Quadratic Equatin", fg="black", font=("Courier",12,"bold")).grid(sticky=N, row=0, columnspan=6)

#take A ---- column = 0
e1 = Entry(frame1, width=15, relief=SUNKEN)
e1.grid(row=0, column=0, padx=10, pady=10)

#write (X^2) ---- labe column = 1
label1 = Label(frame1, height=5, text="X^2  + ", fg="#191970")
label1.grid(row=0, column=1, padx=10, pady=18)

#take B ---- column = 2
e2 = Entry(frame1, width=15, relief=SUNKEN)
e2.grid(row=0, column=2, padx=10, pady=10)

#write (x +) ---- label column = 3
label2 = Label(frame1, text="X + ", fg="#191970")
label2.grid(row=0, column=3, padx=10, pady=10)

#take C ---- column = 4
e3 = Entry(frame1, width=15, relief=SUNKEN)
e3.grid(row=0, column=4, padx=10, pady=10)

#write (= 0) ---- label column = 5
label3 = Label(frame1, text="= 0", fg="#191970")
label3.grid(row=0, column=5, padx=10, pady=10)

#a label that show end answer ----- root answer
label4 = Label(frame1, width=25, relief=RIDGE, highlightbackground="#ADD8E6", highlightthickness=2)
label4.grid(row=1, column=0, padx=3, pady=3, columnspan=3)

#buttons
B_submit = Button(frame1, text="submit", bg="khaki", command=root)
B_submit.grid(row=1, column=2, columnspan=4, padx=10, pady=10, sticky=N)

B_clear = Button(frame1, text="clear", bg="orange", command=clear)
B_clear.grid(row=1, column=3, columnspan=4, padx=10, pady=10, sticky=N)



#-----------BMI-----------

def bmi():
    
    try:
        weight = float(E1.get())
        height = float(E2.get())
        b_bmi = weight / (height**2)
        
        if b_bmi < 18.5:
            label_bmi.config(text="Underweight", fg="darkslateblue")
        elif 18.5 <= b_bmi <= 24.9:
            label_bmi.config(text="Healthy", fg="royalblue")
        elif 25 <= b_bmi <= 29.9:
            label_bmi.config(text="Overweight", fg="khaki")
        elif 30 <= b_bmi <= 39.9:
            label_bmi.config(text="Obese", fg="coral")
        else: 
            label_bmi.config(text="Extremely Obese", fg="maroon")
            
    except ValueError:
        
        messagebox.showerror("Error", "Fill in the blanks correctly or don't click submit")
    
    
def clear2():
    E1.delete(0, END)
    E2.delete(0, END)
    label_bmi.config(text=" ")

#Second Frame          
frame2 = Frame(window, height=50, highlightbackground="black", highlightthickness=2)
frame2.grid(padx=10, pady=10)
l1 = Label(frame2, text="BMI", fg="black", font=("Courier",15,"bold")).grid(sticky=N, row=0, columnspan=5)

# enty weight
E1 = Entry(frame2, width=20, relief=SUNKEN, highlightbackground="black", highlightthickness=2)
E1.grid(row=1, column=1, padx=20, pady=10)

la_w = Label(frame2, text=" weight(kg): ", fg="black").grid(sticky=W, row=1, column=0)

# entry height
E2 = Entry(frame2, width=20, relief=SUNKEN, highlightbackground="black", highlightthickness=2)
E2.grid(row=2, column=1, padx=20, pady=10)

la_h = Label(frame2, text=" height(m): ", fg="black").grid(sticky=W, row=2, column=0)

# age ---- combobox
list_numbes_age = list(range(18,46))
box = ttk.Combobox(frame2, values=list_numbes_age)
box.grid(row=1, column=3, padx=20, pady=10, columnspan=2)
box.insert(0,"Your Age")
box.configure(state="readonly")

# male or female ---- radiobuttons
var = IntVar()
B1 = Radiobutton(frame2, text="Female ", value=1, variable=var).grid(row=2, column=3, pady=5)
B2 = Radiobutton(frame2, text="Male", variable=var, value=2).grid(row=2, column=4, pady=5)

# submit & clear ---- buttons
B_submit = Button(frame2, text="submit", bg="khaki", command=bmi)
B_submit.grid(row=4, column=2, columnspan=4, padx=20, pady=20, sticky=W)

B_clear = Button(frame2, text="clear", bg="orange", command=clear2)
B_clear.grid(row=4, column=3, columnspan=3, padx=20, pady=20, sticky=N)

# frame that show BMI
frame3 = Frame(frame2, relief=SUNKEN, highlightbackground="black", highlightthickness=1, width=200, height=20)
frame3.grid(sticky=N, row=5, columnspan=6, padx=20, pady=20)

label_bmi = Label(frame3, text=" ", font=("Courier", 10, "bold"), width=20, pady=1)
label_bmi.grid(row=0, column=0)

window.mainloop()