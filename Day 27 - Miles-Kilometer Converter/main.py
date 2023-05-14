import tkinter

# Create window
window = tkinter.Tk()
window.title('Mile to Km Converter')
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def calculate():
    miles = float(miles_input.get())
    km = miles * 1.61
    km_result.config(text=f'{km}')


# Miles
miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)
miles_label = tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

equal_label = tkinter.Label(text='is equal to')
equal_label.grid(column=0, row=1)

# Kilometers
km_result = tkinter.Label(text='0')
km_result.grid(column=1, row=1)
km_label = tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = tkinter.Button(text='Calculate', command=calculate)
calculate_button.grid(column=1, row=2)


# Keep window on screen
window.mainloop()
