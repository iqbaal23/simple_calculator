import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

e = tk.Entry(root, width=43, borderwidth=2)
list = []

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def calculate():
    first_num = ""
    sec_num = ""
    list_num = list[0:][::2]
    list_cal = list[1:][::2]
    for x in list_num:
        if first_num == "":
            first_num = x
        else:
            sec_num = x

        if sec_num != "":
            if list_cal[0] == "+":
                hitung = float(first_num) + float(sec_num)
                # print(str(first_num) + " + " + str(sec_num) + " = " + str(hitung))
                result_label['text'] = "= " + str(hitung)
                first_num = hitung
                sec_num = ""
            if list_cal[0] == "-":
                hitung = float(first_num) - float(sec_num)
                # print(str(first_num) + " - " + str(sec_num) + " = " + str(hitung))
                result_label['text'] = "= " + str(hitung)
                first_num = hitung
                sec_num = ""
            if list_cal[0] == "*":
                hitung = float(first_num) * float(sec_num)
                # print(str(first_num) + " * " + str(sec_num) + " = " + str(hitung))
                result_label['text'] = "= " + str(hitung)
                first_num = hitung
                sec_num = ""
            if list_cal[0] == "/":
                hitung = float(first_num) / float(sec_num)
                # print(str(first_num) + " / " + str(sec_num) + " = " + str(hitung))
                result_label['text'] = "= " + str(hitung)
                first_num = hitung
                sec_num = ""
            list_cal.pop(0)



def button_add():
    first_number = e.get()
    list.append(first_number)
    list.append("+")
    e.delete(0, tk.END)
    calculation_label['text'] = list
    calculate()

def button_subtract():
    first_number = e.get()
    list.append(first_number)
    list.append("-")
    e.delete(0, tk.END)
    calculation_label['text'] = list
    calculate()

def button_multiply():
    first_number = e.get()
    list.append(first_number)
    list.append("*")
    e.delete(0, tk.END)
    calculation_label['text'] = list
    calculate()

def button_divide():
    first_number = e.get()
    list.append(first_number)
    list.append("/")
    e.delete(0, tk.END)
    calculation_label['text'] = list
    calculate()

    
def button_equal():
    first_number = e.get()
    list.append(first_number)
    e.delete(0, tk.END)
    calculation_label['text'] = list
    calculate()
    del list[:]

calculation_label = tk.Label(root, text="")
result_label = tk.Label(root, text="=")
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=87, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=78, pady=20, command=button_clear)

button_subtract = tk.Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=41, pady=20, command=button_divide)


calculation_label.grid(row=0, column=0, columnspan=3)
result_label.grid(row=1, column=1, columnspan=3)
e.grid(row=2, column=0, columnspan=3, padx=10,pady=10)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)

button_add.grid(row=7, column=0)
button_equal.grid(row=7, column=1, columnspan=2)

button_subtract.grid(row=8, column=0)
button_multiply.grid(row=8, column=1)
button_divide.grid(row=8, column=2)


root.mainloop()