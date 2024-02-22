import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("ctk öğrenme denemesi1")
app.geometry("600x800")

tabView = customtkinter.CTkTabview(app)
tabView.pack(padx=20, pady=20)

tabView.add("tab-1")
tabView.add("tab-2")
tabView.add("tab-3")
tabView.add("tab-4")

tabView.set("tab-1")
def button_function1():
    print("birinci butona basıldı")

def button_function2():
    print("ikinci butona basıldı")

def button_function3():
    print("üçüncü butona basıldı")

def button_function4():
    print("dördüncü butona basıldı")


button_1 = customtkinter.CTkButton(tabView.tab("tab-1"),text="1. Buton",command=button_function1)
button_1.pack(padx=20, pady=20)

button_2 = customtkinter.CTkButton(tabView.tab("tab-2"),text="2. Buton",command=button_function2)
button_2.pack(padx=20, pady=20)

button_3 = customtkinter.CTkButton(tabView.tab("tab-3"),text="3. Buton",command=button_function3)
button_3.pack(padx=20, pady=20)

button_4 = customtkinter.CTkButton(tabView.tab("tab-4"),text="4. Buton",command=button_function4)
button_4.pack(padx=20, pady=20)



app.mainloop()