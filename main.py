import requests
import tkinter
import customtkinter
from PIL import Image

# api key for open weather api
api_key = 'b4eae007caa0b7facdf7fe531ebb8d88'

# get last searched location
with open("location.txt") as f:
    location = f.read()

# request data for matching cities in GB from open weather geocoding api
coordinates_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location},{"."},{"GB"}&limit=5&appid={api_key}'
coordinates_response = requests.get(coordinates_url)
coordinates_data = coordinates_response.json()

# if request is successful and a match is found
if coordinates_response.status_code == 200 and len(coordinates_data) != 0:

    latitude = coordinates_data[0]['lat']
    longitude = coordinates_data[0]['lon']

    # request data matching for matching latitude and longitude from open weather onecall api
    weather_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}'
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # if request is successful show the current temperature and weather description for the location
    if weather_response.status_code == 200:

        city_and_country = f'{coordinates_data[0]["name"]}, {coordinates_data[0]["state"]}'
        temp_converted_to_c = round(weather_data["current"]["temp"] - 273.15)
        icon_code = weather_data["current"]["weather"][0]["icon"]
        icon_url = 'https://openweathermap.org/img/wn/' + icon_code + '@2x.png'

    # if open weather one call api request is unsuccessful or no match is found
    else:
        city_and_country = 'Location not found'
        temp_converted_to_c = ''

# if open weather geocoding api request is unsuccessful or no match is found
else:
    city_and_country = 'Location not found'
    temp_converted_to_c = ''

# set custom tkinter dark theme
mode = "dark"
mode = customtkinter.set_appearance_mode(mode)

# create custom tkinter window
window = customtkinter.CTk()

# set window width and height
window.geometry("400x400")

# set window title
window.title("weatherology")
# heading
heading_label = customtkinter.CTkLabel(master=window, font=("courier", 24), text_color=("#C63D2F", "#FFBB5C"), text="⚡ weatherology ⚡")
heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


# light/dark mode button
def change_mode():
    global mode

    if mode == "light":
        customtkinter.set_appearance_mode("dark")
        mode = "dark"
    else:
        customtkinter.set_appearance_mode("light")
        mode = "light"


search_submit = customtkinter.CTkButton(master=window,
                                        width=45,
                                        fg_color="#E25E3E",
                                        hover_color="#C63D2F",
                                        text="mode",
                                        command=change_mode)

search_submit.place(relx=0.87, rely=0.05, anchor=customtkinter.W)

# search input field
search_input = customtkinter.CTkEntry(window, width=200, placeholder_text="search for a city")
search_input.place(relx=0.1, rely=0.25, anchor=tkinter.W)


# submit button
def search():
    search_location = search_input.get()

    # request data for matching cities in GB from open weather geocoding api
    coordinates_url = f'http://api.openweathermap.org/geo/1.0/direct?q={search_location},{"."},{"GB"}&limit=5&appid={api_key}'
    coordinates_response = requests.get(coordinates_url)
    coordinates_data = coordinates_response.json()

    # if request is successful and a match is found

    if coordinates_response.status_code == 200 and len(coordinates_data) != 0:

        latitude = coordinates_data[0]['lat']
        longitude = coordinates_data[0]['lon']

        # request data matching for matching latitude and longitude from open weather onecall api
        weather_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={api_key}'
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # if request is successful show the current temperature and weather description for the location
        if weather_response.status_code == 200:
            # searched location saved to location.txt so that this will be the location displayed next time the app is run
            with open("location.txt", "w") as f:
                f.write(search_location)

            city_and_country = f'{coordinates_data[0]["name"]}, {coordinates_data[0]["state"]}'
            temp_converted_to_c = round(weather_data["current"]["temp"] - 273.15)
            icon_code = weather_data["current"]["weather"][0]["icon"]
            icon_url = 'https://openweathermap.org/img/wn/' + icon_code + '@2x.png'


            # temperature
            temp_label = customtkinter.CTkLabel(master=window, font=("", 60), width=400,
                                                text=f'{temp_converted_to_c}{chr(176)}C', anchor=tkinter.W)
            temp_label.place(relx=0.1, rely=0.7, anchor=tkinter.W)

            # weather icon
            icon_response = requests.get(icon_url)
            icon = icon_response.content
            with open("icon.png", "wb") as f:
                f.write(icon)
                f.close()
            weather_icon = customtkinter.CTkImage(dark_image=Image.open("icon.png"), size=(150, 150))
            weather_icon_label = customtkinter.CTkLabel(window, image=weather_icon, width=200,
                                                        text="", anchor=tkinter.W)
            weather_icon_label.place(relx=0.5, rely=0.7, anchor=tkinter.W)

            # location name
            location_label = customtkinter.CTkLabel(master=window, font=("", 24), width=400,
                                                    text=f'{city_and_country}', anchor=tkinter.W)
            location_label.place(relx=0.1, rely=0.5, anchor=tkinter.W)

        # if open weather one call api request is unsuccessful or no match is found
        else:
            city_and_country = 'Location not found'
            temp_converted_to_c = ''
            # temperature
            temp_label = customtkinter.CTkLabel(master=window, font=("", 60), width=400,
                                                text=f'{temp_converted_to_c}', anchor=tkinter.W)
            temp_label.place(relx=0.1, rely=0.7, anchor=tkinter.W)

            # weather icon
            weather_icon_label = customtkinter.CTkLabel(window, width=200,
                                                        text="", anchor=tkinter.W)
            weather_icon_label.place(relx=0.5, rely=0.7, anchor=tkinter.W)

            # location name
            location_label = customtkinter.CTkLabel(master=window, font=("", 24), height=150, width=400,
                                                    text=f'{city_and_country}', anchor=tkinter.W)
            location_label.place(relx=0.1, rely=0.5, anchor=tkinter.W)

    # if open weather geocoding api request is unsuccessful or no match is found
    else:
        city_and_country = 'Location not found'
        temp_converted_to_c = ''
        # temperature
        temp_label = customtkinter.CTkLabel(master=window, font=("", 60), height=150, width=400,
                                            text=f'{temp_converted_to_c}', anchor=tkinter.W)
        temp_label.place(relx=0.1, rely=0.7, anchor=tkinter.W)

        # weather icon
        weather_icon_label = customtkinter.CTkLabel(window, width=200,
                                                    text="", anchor=tkinter.W)
        weather_icon_label.place(relx=0.5, rely=0.7, anchor=tkinter.W)

        # location name
        location_label = customtkinter.CTkLabel(master=window, font=("", 24), width=400,
                                                text=f'{city_and_country}', anchor=tkinter.W)
        location_label.place(relx=0.1, rely=0.5, anchor=tkinter.W)


search_submit = customtkinter.CTkButton(master=window,
                                        width=100,
                                        fg_color="#E25E3E",
                                        hover_color="#C63D2F",
                                        text="submit",
                                        command=search)

search_submit.place(relx=0.65, rely=0.25, anchor=customtkinter.W)

# temperature
temp_label = customtkinter.CTkLabel(master=window, font=("", 60), width=400,
                                    text=f'{temp_converted_to_c}{chr(176)}C', anchor=tkinter.W)
temp_label.place(relx=0.1, rely=0.7, anchor=tkinter.W)

# weather icon
icon_response = requests.get(icon_url)
icon = icon_response.content
with open("icon.png", "wb") as f:
    f.write(icon)
    f.close()

weather_icon = customtkinter.CTkImage(dark_image=Image.open("icon.png"), size=(150, 150))
weather_icon_label = customtkinter.CTkLabel(window, image=weather_icon, width=200,
                                            text="", anchor=tkinter.W)
weather_icon_label.place(relx=0.5, rely=0.7, anchor=tkinter.W)

# location name
location_label = customtkinter.CTkLabel(master=window, font=("", 24), width=400,
                                        text=f'{city_and_country}', anchor=tkinter.W)
location_label.place(relx=0.1, rely=0.5, anchor=tkinter.W)

window.mainloop()
