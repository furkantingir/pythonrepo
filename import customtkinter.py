import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()

app.title("ctk öğrenme denemesi1")
app.geometry("600x800")

frame = customtkinter.CTkFrame(master=app,
                               width=200,
                               height=200,
                               corner_radius=15,
                               bg_color="transparent",
                               border_color="green",
                               border_width=5
                               
                               
                               )
                               



frame.pack(padx=20, pady=20)



def button1_function():
    print("a")

def button2_function():
    print("b")



button1 = customtkinter.CTkButton(master=frame, text="buton1",command= button1_function)

button1.place(relx=0.5, rely=0.4, anchor = tkinter.CENTER)

button2 = customtkinter.CTkButton(master=frame, text="buton2",command= button2_function)
button2.place(relx=0.5, rely=0.6, anchor = tkinter.CENTER)



app.mainloop()