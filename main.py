import tkinter

window = tkinter.Tk()

window.title("Mile to Km Convertor")
window.config(padx=40,pady=40)
label = tkinter.Label(text="Miles")
label.grid(column=3,row=1)
label = tkinter.Label(text="Km")
label.grid(column=3,row=2)
label = tkinter.Label(text="is equal to")
label.grid(column=0,row=2)
label2 = tkinter.Label(text="0")
label2.grid(column=1,row=2)

window.minsize(width=300, height=150)
def click_fun():
    new_text = float(input.get())*1.609344
    label2.config(text=round(new_text))
button = tkinter.Button(text="Calculate", command=click_fun)
button.grid(column=1,row=4)
input = tkinter.Entry(width=6)
input.grid(column=1,row=1)
window.mainloop()