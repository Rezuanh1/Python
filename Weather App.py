import os
from dotenv import load_dotenv
import requests
import customtkinter as ctk
from tkinter import messagebox


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']

        result = (
            f"📍 {city_name}, {country}\n"
            f"🌡️ Temp: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁️ Weather: {weather}"
        )
        output_label.configure(text=result)

    else:
        messagebox.showerror("Error", "City not found!")


ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🌤️ Modern Weather App")
app.geometry("500x350")
app.resizable(False, False)


title_label = ctk.CTkLabel(app, text="🌍 Weather App", font=("Arial", 22, "bold"))
title_label.pack(pady=15)


city_entry = ctk.CTkEntry(app, placeholder_text="Enter City Name", width=300, height=40, font=("Arial", 14))
city_entry.pack(pady=10)


search_btn = ctk.CTkButton(app, text="Get Weather", command=get_weather, width=200, height=40, fg_color="green")
search_btn.pack(pady=15)


output_label = ctk.CTkLabel(app, text="", font=("Arial", 16), justify="left")
output_label.pack(pady=20)

app.mainloop()
