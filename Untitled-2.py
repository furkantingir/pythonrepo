import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("ctk öğrenme denemesi1")
app.geometry("600x800")



def button_function():
    print("a")



button = customtkinter.CTkButton(master=app, text="Deneme")
button.place(relx=0.5, rely=0.8, anchor = tkinter.CENTER)









app.mainloop()