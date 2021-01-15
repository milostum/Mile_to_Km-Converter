from tkinter import *


def convert_miles_to_km():
    km_output = round((float(miles_input.get()) * 1.609344), 2)
    covert_label.config(text=f"{km_output}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

label_is_equal = Label(text="is equal to", font=("Arial", 12))
label_is_equal.grid(column=0, row=1)
label_is_equal.config(padx=10, pady=10)

label_miles = Label(text="Miles", font=("Arial", 12))
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km = Label(text="Km", font=("Arial", 12))
label_km.grid(column=2, row=1)
label_km.config(padx=10, pady=10)

covert_label = Label(text="0", font=("Arial", 12))
covert_label.grid(column=1, row=1)
covert_label.config(padx=10, pady=10)

miles_input = Entry(width=10, font=("Arial", 12))
miles_input.grid(column=1, row=0)

button = Button(text="Calculate", font=("Arial", 12), command=convert_miles_to_km, fg="blue", bg="lightblue")
button.grid(column=1, row=2)

window.mainloop()
