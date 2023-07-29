import tkinter
import tkinter.messagebox
import sys 
import requests
import json
from datetime import datetime
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
def cityenter():
    print(entry.get())
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q="+entry.get()+"&appid=568c7afedc03b362c7573f8e30486cc9")
    print(response.json())
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1000x600")
app.resizable(0,0)
entry = customtkinter.CTkEntry(app, width=140, height=30,placeholder_text="Podaj miasto", )
entry.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
button1 =customtkinter.CTkButton(app, width=30, height=30,text='>', command = cityenter)
button1.place(relx=0.59, rely=0.05, anchor=customtkinter.CENTER)


app.mainloop()
