from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)

input = Entry(width=7)
input.pack()
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row = 0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row = 1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row = 1)

kilometer_label = Label(text="KM")
kilometer_label.grid(column=2, row = 1)
def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

button = Button(text="Calculate", command=miles_to_km())

window.mainloop()