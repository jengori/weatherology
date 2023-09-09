# import libraries
import requests


# this class is responsible for retrieving the weather icon via a URL and saving it to the icon.png file
class IconHandler:

    def __init__(self, icon_url):
        self.icon_url = icon_url

    def save_icon(self):
        icon_response = requests.get(self.icon_url)
        icon = icon_response.content
        with open("icon.png", "wb") as f:
            f.write(icon)
            f.close()
