import tkinter
MILES_TO_KM = 1.609
KM_TO_MILES = 1/1.609
INCH_TO_FEET = 1/12
FEET_TO_INCH = 12
window  = tkinter.Tk()
window.title("Unit_converter")
window.title("Unit Converter")
window.config(padx=20, pady=20)

my_label = tkinter.Label()
my_label.config(text="is equal to", font=("Arial"))
my_label.grid(column=1, row=2)



km_label = tkinter.Label()
km_label.config(text="km", font=("Arial"))
km_label.grid(column=3, row=2)
answer = tkinter.Label()
answer.config(text=" ", font=("Arial"))
answer.grid(column=2, row=2)
def convert_units():
    conversionval = 0
    if listbox.get(listbox.curselection()) == "mile to kilo":
        conversionval = MILES_TO_KM
    elif listbox.get(listbox.curselection()) == "kilo to mile":
        conversionval = KM_TO_MILES
    elif listbox.get(listbox.curselection()) == "inches to feet":
        conversionval = INCH_TO_FEET
    elif listbox.get(listbox.curselection()) == "feet to inches":
        conversionval = 12
    new_val = float(my_input.get()) * conversionval
    answer.config(text=f"{new_val}")


my_button = tkinter.Button(text="Convert to Km", command = convert_units)
my_button.grid(column=2, row=3)

my_input = tkinter.Entry()
my_input.grid(column=2, row=1)

def set_conversion(event):
    # Gets current selection from listbox
    _ = listbox.get(listbox.curselection())
    my_button.config(text=_)

listbox = tkinter.Listbox(height=4)
conversions = ["mile to kilo", "kilo to mile", "inches to feet", "feet to inches"]
for item in conversions:
    listbox.insert(conversions.index(item), item)
listbox.bind("<<ListboxSelect>>", set_conversion)
listbox.grid(column=2, row=4)
window.mainloop()
