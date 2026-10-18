# ================= Project: Math & Health Tools =================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# ================= 1. Quadratic Equation Solver =================
def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        delta = (b*b) - (4*a*c)
        
        if delta > 0:
            x1 = (-b + delta**.5) / (2*a)
            x2 = (-b - delta**.5) / (2*a)
            quad_result_label.config(text=f"X1 = {x1:.2f}  &  X2 = {x2:.2f}", fg="blue")
        elif delta == 0:
            x = -b / (a*2)
            quad_result_label.config(text=f"X = {x:.2f}", fg="yellow")
        else:
            quad_result_label.config(text="Bedone Rishe (delta < 0)", fg="red")
            
    except ValueError:
        messagebox.showerror("Error", "Fill in the blanks or don't click submit")
        
def clear_quadratic():
    entry_a.delete(0, END)
    entry_b.delete(0, END)
    entry_c.delete(0, END)
    quad_result_label.config(text="")
    
# ================= Main Window Setup =================
window = Tk()
window.title("Project")
window.configure(bg="pink")
window.geometry("520x470")

# --- UI: Quadratic Equation Section ---
frame_quad = Frame(window, height=50, highlightbackground="black", highlightthickness=2)
frame_quad.grid(padx=10, pady=10)

# Section Title
lbl_title_quad = Label(frame_quad, text="Solve The Quadratic Equation", fg="black", font=("Courier",12,"bold"))
lbl_title_quad.grid(sticky=N, row=0, columnspan=6)

# Input for 'a'
entry_a = Entry(frame_quad, width=15, relief=SUNKEN)
entry_a.grid(row=0, column=0, padx=10, pady=10)

# Label for 'X^2'
lbl_x_squared = Label(frame_quad, height=5, text="X^2  + ", fg="#191970")
lbl_x_squared.grid(row=0, column=1, padx=10, pady=18)

# Input for 'b'
entry_b = Entry(frame_quad, width=15, relief=SUNKEN)
entry_b.grid(row=0, column=2, padx=10, pady=10)

# Label for 'X'
lbl_x = Label(frame_quad, text="X + ", fg="#191970")
lbl_x.grid(row=0, column=3, padx=10, pady=10)

# Input for 'c'
entry_c = Entry(frame_quad, width=15, relief=SUNKEN)
entry_c.grid(row=0, column=4, padx=10, pady=10)

# Label for '= 0'
lbl_equals_zero = Label(frame_quad, text="= 0", fg="#191970")
lbl_equals_zero.grid(row=0, column=5, padx=10, pady=10)

# Result Display
quad_result_label = Label(frame_quad, width=25, relief=RIDGE, highlightbackground="#ADD8E6", highlightthickness=2)
quad_result_label.grid(row=1, column=0, padx=3, pady=3, columnspan=3)

# Action Buttons
btn_quad_submit = Button(frame_quad, text="submit", bg="khaki", command=solve_quadratic)
btn_quad_submit.grid(row=1, column=2, columnspan=4, padx=10, pady=10, sticky=N)

btn_quad_clear = Button(frame_quad, text="clear", bg="orange", command=clear_quadratic)
btn_quad_clear.grid(row=1, column=3, columnspan=4, padx=10, pady=10, sticky=N)


# ================= 2. BMI Calculator =================
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        b_bmi = weight / (height**2)
        
        if b_bmi < 18.5:
            bmi_result_label.config(text="Underweight", fg="darkslateblue")
        elif 18.5 <= b_bmi <= 24.9:
            bmi_result_label.config(text="Healthy", fg="royalblue")
        elif 25 <= b_bmi <= 29.9:
            bmi_result_label.config(text="Overweight", fg="khaki")
        elif 30 <= b_bmi <= 39.9:
            bmi_result_label.config(text="Obese", fg="coral")
        else: 
            bmi_result_label.config(text="Extremely Obese", fg="maroon")
            
    except ValueError:
        messagebox.showerror("Error", "Fill in the blanks correctly or don't click submit")
    
    
def clear_bmi():
    entry_weight.delete(0, END)
    entry_height.delete(0, END)
    bmi_result_label.config(text=" ")

# --- UI: BMI Calculator Section ---
frame_bmi = Frame(window, height=50, highlightbackground="black", highlightthickness=2)
frame_bmi.grid(padx=10, pady=10)

# Section Title
lbl_title_bmi = Label(frame_bmi, text="BMI", fg="black", font=("Courier",15,"bold"))
lbl_title_bmi.grid(sticky=N, row=0, columnspan=5)

# Weight Input & Label
entry_weight = Entry(frame_bmi, width=20, relief=SUNKEN, highlightbackground="black", highlightthickness=2)
entry_weight.grid(row=1, column=1, padx=20, pady=10)

lbl_weight = Label(frame_bmi, text=" weight(kg): ", fg="black")
lbl_weight.grid(sticky=W, row=1, column=0)

# Height Input & Label
entry_height = Entry(frame_bmi, width=20, relief=SUNKEN, highlightbackground="black", highlightthickness=2)
entry_height.grid(row=2, column=1, padx=20, pady=10)

lbl_height = Label(frame_bmi, text=" height(m): ", fg="black")
lbl_height.grid(sticky=W, row=2, column=0)

# Age Combobox
list_numbes_age = list(range(18,46))
combo_age = ttk.Combobox(frame_bmi, values=list_numbes_age)
combo_age.grid(row=1, column=3, padx=20, pady=10, columnspan=2)
combo_age.insert(0,"Your Age")
combo_age.configure(state="readonly")

# Gender Radiobuttons
gender_var = IntVar()
radio_female = Radiobutton(frame_bmi, text="Female ", value=1, variable=gender_var)
radio_female.grid(row=2, column=3, pady=5)

radio_male = Radiobutton(frame_bmi, text="Male", variable=gender_var, value=2)
radio_male.grid(row=2, column=4, pady=5)

# Action Buttons
btn_bmi_submit = Button(frame_bmi, text="submit", bg="khaki", command=calculate_bmi)
btn_bmi_submit.grid(row=4, column=2, columnspan=4, padx=20, pady=20, sticky=W)

btn_bmi_clear = Button(frame_bmi, text="clear", bg="orange", command=clear_bmi)
btn_bmi_clear.grid(row=4, column=3, columnspan=3, padx=20, pady=20, sticky=N)

# Result Display Frame
frame_bmi_result = Frame(frame_bmi, relief=SUNKEN, highlightbackground="black", highlightthickness=1, width=200, height=20)
frame_bmi_result.grid(sticky=N, row=5, columnspan=6, padx=20, pady=20)

bmi_result_label = Label(frame_bmi_result, text=" ", font=("Courier", 10, "bold"), width=20, pady=1)
bmi_result_label.grid(row=0, column=0)

window.mainloop()