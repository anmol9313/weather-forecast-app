from tkinter import *
from tkinter import ttk
import requests

def data_get():
    # FIXED: Indented the function body properly and wrapped the API request/updates inside it
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=f437ab668e4e6c7a101579efac47c033").json()

    weather_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15))+"°C")
    speed_label1.config(text=str(data["wind"]["speed"])+" m/s")

win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("500x500")
name_label = Label(win, text="Weather Forecast", bg="lightblue", font=("Arial", 35, "bold"))
name_place = name_label.place(x=50, y=50)

city_name = StringVar()
# FIXED: Changed "city_name" string to the actual city_name variable object
com = ttk.Combobox(win,text="weather", values=["Select City", "Surat", "Ahmedabad", "rajkot", "mumbai", "delhi", "bangalore", "pune", "chennai"] ,textvariable=city_name) 
com.place(x=150, y=150, width=200 , height=30)
com.set("Select City")


weather_label = Label(win, text="Weather Climate: ", bg="lightblue", font=("Arial", 15))
weather_label.place(x=100, y=300)
weather_label1 = Label(win, text=" ", bg="lightblue", font=("Arial", 15))
weather_label1.place(x=260, y=300 ,width=200 , height=30)

wb_label = Label(win, text="Weather Nature: ", bg="lightblue", font=("Arial", 15))
wb_label.place(x=100, y=350)
wb_label1 = Label(win, text=" ", bg="lightblue", font=("Arial", 15))
wb_label1.place(x=260, y=350 ,width=200 , height=30)

temp_label = Label(win, text="Temperature: ", bg="lightblue", font=("Arial", 15))
temp_label.place(x=100, y=400)
temp_label1 = Label(win, text=" ", bg="lightblue", font=("Arial", 15))
temp_label1.place(x=260, y=400 ,width=200 , height=30)

speed_label = Label(win, text="Wind Speed: ", bg="lightblue", font=("Arial", 15))
speed_label.place(x=100, y=450)
speed_label1 = Label(win, text=" ", bg="lightblue", font=("Arial", 15))
speed_label1.place(x=260, y=450 ,width=200 , height=30)

# FIXED: Added command=data_get so the button triggers the function when clicked
done_button = Button(win, text="Get Weather", bg="blue", fg="white", font=("Arial", 15, "bold"), command=data_get)
done_button.place(x=150, y=200, width=150, height=30)

win.mainloop()