import tkinter
import tkinter.messagebox
import sys 
import requests
import json
from datetime import datetime
import customtkinter
from PIL import Image
import os

weather="static/images/error.png"
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
def cityenter():
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q="+entry.get()+"&appid=568c7afedc03b362c7573f8e30486cc9")
    data =response.json()
    cityname = data['city']['name']
    weather_state=data['list'][0]['weather'][0]['main']
    temp_state = round(data['list'][0]['main']['temp']/10,1)
    weather_output = "Today in " + cityname +", there is " + weather_state.lower()+". The temperature is " + str(temp_state)+"°C."
    city_textbox.delete("0.0", "end")
    city_textbox.insert("5.5", weather_output)
    city_textbox.configure(state="disabled")
    print(cityname)
    print(weather_output)
    if weather_state=="Rain":
        weather='static/images/rain.png'
    elif weather_state=="Sun" or weather_state=='Clear':
        weather='static/images/sun.png'
    elif weather_state=="Clouds":
        weather='static/images/cloud.png'
    else:
        weather='static/images/error.png'

    weather_img = customtkinter.CTkImage(light_image=Image.open(os.path.join(weather)), size=(50 , 50))    
    image_label = customtkinter.CTkLabel(app, image=weather_img, text="")  # display image with a CTkLabel
    image_label.place(relx=0.45, rely=0.3)
    temp_textbox = customtkinter.CTkLabel(app,width=380, height=30, corner_radius=0.7,justify='center', text=str(temp_state) + "°C", font=("Arial", 25))
    temp_textbox.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER,)


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x600")
app.resizable(0,0)
app.title("Weather by Myszor")
entry = customtkinter.CTkEntry(app, width=140, height=30,placeholder_text="Podaj miasto",corner_radius=10)
entry.place(relx=0.5, rely=0.05, anchor=customtkinter.CENTER)
button1 =customtkinter.CTkButton(app, width=30, height=30,text='>', command = cityenter, corner_radius=10)
button1.place(relx=0.713, rely=0.05, anchor=customtkinter.CENTER)
city_textbox = customtkinter.CTkTextbox(app,width=380, height=30, corner_radius=0.7,border_width=0,fg_color='transparent')
city_textbox.place(relx=0.5, rely=0.11, anchor=customtkinter.CENTER,)



app.mainloop()
