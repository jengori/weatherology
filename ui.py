# import libraries
import tkinter
import customtkinter
from PIL import Image
# import classes
from api import ApiCaller
from icon_handler import IconHandler

APP_NAME = "⚡ weatherology ⚡"
WINDOW_DIMENSIONS = "400x400"
DEFAULT_MODE = "dark"


# this class creates and updates the UI
class Ctk:
    def __init__(self):

        # set appearance mode, create window
        self.mode = DEFAULT_MODE
        customtkinter.set_appearance_mode(self.mode)
        self.window = customtkinter.CTk()
        self.window.geometry(WINDOW_DIMENSIONS)
        self.window.title(APP_NAME)

        # heading label
        self.heading_label = customtkinter.CTkLabel(master=self.window,
                                                    font=("courier", 24),
                                                    text_color=("#C63D2F", "#FFBB5C"),
                                                    text=APP_NAME)
        self.heading_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        # button to change between light and dark mode
        self.mode_button = customtkinter.CTkButton(master=self.window,
                                                   width=45,
                                                   fg_color="#E25E3E",
                                                   hover_color="#C63D2F",
                                                   text="mode",
                                                   command=self.change_mode)

        self.mode_button.place(relx=0.87,
                               rely=0.05,
                               anchor=customtkinter.W)

        # search field
        self.search_field = customtkinter.CTkEntry(self.window,
                                                   width=200,
                                                   placeholder_text="search for a city")
        self.search_field.place(relx=0.1,
                                rely=0.25,
                                anchor=tkinter.W)

        # submit button
        submit_button = customtkinter.CTkButton(master=self.window,
                                                width=100,
                                                fg_color="#E25E3E",
                                                hover_color="#C63D2F",
                                                text="submit",
                                                command=self.search)

        submit_button.place(relx=0.65,
                            rely=0.25,
                            anchor=customtkinter.W)

    # method to change between light and dark mode
    def change_mode(self):
        if self.mode == "light":
            customtkinter.set_appearance_mode("dark")
            self.mode = "dark"
        else:
            customtkinter.set_appearance_mode("light")
            self.mode = "light"

    # method to get input from search field when submit button is clicked
    def search(self):
        # get input from search field
        new_loc = self.search_field.get()
        # instantiate ApiCaller object
        new_caller = ApiCaller(new_loc)
        # if location found
        if new_caller.coordinates_data:
            # write location name to location.txt
            with open("location.txt", "w") as f:
                f.write(new_loc)
            # display location, temperature and weather icon
            self.show_temp(new_caller.temp_converted_to_c)
            new_icon_handler = IconHandler(new_caller.icon_url)
            new_icon_handler.save_icon()
            self.show_icon("icon.png")
            self.show_location(new_caller.location_string)

        else:
            self.show_message()

    # method to display temperature
    def show_temp(self, temp):
        temp_label = customtkinter.CTkLabel(master=self.window,
                                            font=("", 60),
                                            width=400,
                                            text=f'{temp}{chr(176)}C',
                                            anchor=tkinter.W)
        temp_label.place(relx=0.1,
                         rely=0.7,
                         anchor=tkinter.W)

    # method to display weather icon
    def show_icon(self, icon_file):
        weather_icon = customtkinter.CTkImage(dark_image=Image.open(icon_file),
                                              size=(150, 150))
        weather_icon_label = customtkinter.CTkLabel(self.window,
                                                    image=weather_icon,
                                                    width=200,
                                                    text="",
                                                    anchor=tkinter.W)
        weather_icon_label.place(relx=0.5,
                                 rely=0.7,
                                 anchor=tkinter.W)

    # display location label
    def show_location(self, loc_string):
        location_label = customtkinter.CTkLabel(master=self.window,
                                                font=("", 24),
                                                width=400,
                                                text=loc_string,
                                                anchor=tkinter.W)
        location_label.place(relx=0.1,
                             rely=0.5,
                             anchor=tkinter.W)

    # display location not found message
    def show_message(self):
        message_label = customtkinter.CTkLabel(master=self.window,
                                               font=("", 24),
                                               width=400,
                                               height=400,
                                               text="Location not found",
                                               anchor=tkinter.NW)
        message_label.place(relx=0.1,
                            rely=0.45,
                            anchor=tkinter.NW)













