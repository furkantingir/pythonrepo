import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("ctk öğrenme denemesi1")
app.geometry("600x800")

textbox= customtkinter.CTkTextbox(app)

textbox.place(relx=0.4 , rely=0.4 , anchor = tkinter.CENTER)


text="""
           ft deneme yapıyor

"""
textbox.insert("0.0",text)
textbox.configure(state="normal")

def button_func1():
   print(textbox.get("0.0","end"))

button1 = customtkinter.CTkButton(master=app, text="button", command= button_func1)
button1.place(relx=0.4,rely=0.5, anchor = tkinter.CENTER)








app.mainloop()