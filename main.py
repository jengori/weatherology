# import Ctk and ApiCaller classes
from ui import Ctk
from api import ApiCaller
from icon_handler import IconHandler

DEFAULT_LOCATION = "London"

# get last searched location (or default location if none)
with open("location.txt") as f:
    location = f.read()
    if location == "":
        location = DEFAULT_LOCATION

# instantiate ui and caller objects
ui = Ctk()
caller = ApiCaller(location)

# if location found
if caller.coordinates_data:
    # download weather icon and save in icon.png file
    icon_handler = IconHandler(caller.icon_url)
    icon_handler.save_icon()

    # display temperature, weather icon and location on ui
    ui.show_temp(caller.temp_converted_to_c)
    ui.show_icon("icon.png")
    ui.show_location(caller.location_string)
else:
    # display location not found message
    ui.show_message()

ui.window.mainloop()
