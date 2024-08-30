import tkinter as tk
from tkinter import PhotoImage, Label, Text, Button, RAISED, END
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import parse



root = tk.Tk()
root.geometry("600x200")
root.title("Phone Teller")
root.config(background='#161717')


icon = PhotoImage(file='Airplane.png')
root.iconphoto(True, icon)


label1 = Label(root, text="Phone Teller", font=('Futurism', 20), fg='#03f8fc', bg='#161717')
label1.pack()


def get_result():
    num = number.get("1.0", END).strip()
    num1 = parse(num)

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    result_textbox.insert(END, f"The Country of this number is: {location}\n")
    result_textbox.insert(END, f"The Sim Card of this number is: {service_provider}\n")


number = Text(root, height=1, fg='#03f8fc', bg='black', relief=RAISED, bd=7)
number.pack()


button = Button(root, text="Search", command=get_result, font=('Futurism', 10), fg='#03f8fc', bg='black',
                activeforeground='#03f8fc', activebackground="black", relief=RAISED, bd=7)
button.pack(pady=10, padx=10)


result_textbox = Text(root, height=7, fg='#03f8fc', bg='black', relief=RAISED, bd=7)
result_textbox.pack()

# Run the main loop
root.mainloop()
