import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("ctk öğrenme denemesi1")
app.geometry("600x800")

frame = customtkinter.CTkFrame(master=app,
                               width=200,
                               height=200,
                               corner_radius=10)
frame.pack(padx=20, pady=20)

tk_textbox = tkinter.Text(frame, highlightthickness=0 )
tk_textbox.grid(row=0, column=0 , sticky="nsew")

ctk_textbox_scrollbar = customtkinter.CTkScrollbar(frame, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="nsew")

tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

def button_func1():
   print(tk_textbox.get("0.0","end"))

button1 = customtkinter.CTkButton(master=frame, text="button", command= button_func1)
button1.grid(padx=20, pady=10)


app.mainloop()