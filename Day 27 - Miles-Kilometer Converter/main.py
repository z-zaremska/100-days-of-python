from tkinter import Label, Entry, Button, Tk

# Create window
window = Tk()
window.title('Mile to Km Converter')
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_input.get())
    km = miles * 1.61
    km_result.config(text=f'{km}')


# Miles
miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

# Kilometers
km_result = Label(text='0')
km_result.grid(column=1, row=1)
km_label = Label(text='Km')
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)

# Keep window on screen
window.mainloop()
