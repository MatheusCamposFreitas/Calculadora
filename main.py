from tkinter import * 
from tkinter import ttk

window_bg_color = "#3b3b3b"
frame_bg_color = "#38576b"
button_Clean_bg = "#ECEFF1"
button_operation_bg = "#FFAB40"
font_white = "#feffff"

window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=window_bg_color)

frame_display = Frame(window, width=235, height=50, bg=frame_bg_color)
frame_display.grid(row=0, column=0)

frame_keyboard = Frame(window, width=235, height=268)
frame_keyboard.grid(row=1, column=0)


expression = ''
value_text = StringVar()

def input_value(event):
    global expression
    expression = expression + str(event)
    value_text.set(expression)


def calcular():
    result = eval(expression)
    value_text.set(str(result))


def clear_frame():
    global expression
    expression = ""
    value_text.set("")


frame_label = Label(frame_display, textvariable=value_text, width=15, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18 bold'), bg=frame_bg_color, fg=font_white)
frame_label.place(x=0, y=0)

button_Clean = Button(frame_keyboard, command=clear_frame, text="C", width=12, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Clean.place(x=0, y=0)

button_Modulus = Button(frame_keyboard, command= lambda: input_value('%'), text="%", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Modulus.place(x=118, y=0)

button_Division = Button(frame_keyboard, command= lambda: input_value('/'), text="/", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Division.place(x=177, y=0)

button_number7 = Button(frame_keyboard, command= lambda: input_value('7'), text="7", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number7.place(x=0, y=52)

button_number8 = Button(frame_keyboard, command= lambda: input_value('8'), text="8", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number8.place(x=59, y=52)

button_number9 = Button(frame_keyboard, command= lambda: input_value('9'), text="9", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number9 .place(x=118, y=52)

button_Multiplication = Button(frame_keyboard, command= lambda: input_value('*'), text="*", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Multiplication.place(x=177, y=52)


button_number4 = Button(frame_keyboard, command= lambda: input_value('4'), text="4", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number4.place(x=0, y=104)

button_number5 = Button(frame_keyboard, command= lambda: input_value('5'), text="5", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number5.place(x=59, y=104)

button_number6 = Button(frame_keyboard, command= lambda: input_value('6'), text="6", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number6 .place(x=118, y=104)

button_Subtraction = Button(frame_keyboard, command= lambda: input_value('-'), text="-", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Subtraction.place(x=177, y=104)

button_number1 = Button(frame_keyboard, command= lambda: input_value('1'), text="1", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number1.place(x=0, y=156)

button_number2 = Button(frame_keyboard, command= lambda: input_value('2'), text="2", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number2.place(x=59, y=156)

button_number3 = Button(frame_keyboard, command= lambda: input_value('3'), text="3", width=6, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number3 .place(x=118, y=156)

button_Addition = Button(frame_keyboard, command= lambda: input_value('+'), text="+", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Addition.place(x=177, y=156)


button_number0 = Button(frame_keyboard, command= lambda: input_value('0'), text="0", width=12, height=2, bg=button_Clean_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_number0.place(x=0, y=208)

button_Dot = Button(frame_keyboard, command= lambda: input_value('.'), text=".", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Dot.place(x=118, y=208)

button_Equal = Button(frame_keyboard, command= calcular, text="=", width=6, height=2, bg=button_operation_bg, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_Equal.place(x=177, y=208)




window. mainloop()
