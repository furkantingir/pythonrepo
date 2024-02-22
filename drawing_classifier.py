from customtkinter import *

app = CTk()
app.geometry("500x400")

set_default_color_theme("blue")

def change_handler(value):
    print(f"Selected Value {value}")
    

btn = CTkSlider(master=app, from_=0, to=100, command=change_handler)

btn.place(relx=0.5, rely=0.5, anchor="center") 


CTkButton(master=app, text="Button").pack(pady=20, padx=20)
CTkCheckBox(master=app, text="Check box").pack(pady=20, padx=20)
CTkComboBox(master=app, values=["Option 1", "Option 2", "Option 3"]).pack(pady=20, padx=20)
CTkEntry(master=app, placeholder_text="Start typing...").pack(pady=20, padx=20)
CTkRadioButton(master=app, text="Radio button").pack(pady=20, padx=20)

CTkSwitch(master=app, text="Option").pack(pady=20, padx=20)


app.mainloop()