#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com


import json
from easygui import *
import sys
import urllib.request  # install it with : pip3 install urllib3


# class creation
class People:
    def __init__(self):
        self.name = "default"
        self.spacecraft = "default"
        self.number = 0
        self.image = "spacecraft.gif"


# variables creation
def parser():
    name = ""
    People.image = "spacecraft.gif"
    urlData = "http://api.open-notify.org/astros.json"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset("utf-8")
    space = json.loads(data.decode(encoding))
    People.number = space["number"]
    if space["message"] == "success":
        for i in space["people"]:
            People.name = i["name"]
            People.spacecraft = i["craft"]
            name = name + (
                ("Name of the astronaut : ")
                + str(People.name)
                + str("\n\n")
                + str("Spacecraft : ")
                + str(People.spacecraft)
                + str("\n\n")
            )

        msg = (
            ("This software show in real-time how many people are in space.\n\n")
            + str("Number of people in space : ")
            + str(People.number)
            + str("\n\n")
            + (name)
        )
        choices = ["Close"]
        reply = buttonbox(msg, image=People.image, choices=choices)
        if reply == "Close":
            sys.exit(0)
        else:
            sys.exit(0)

    else:
        msg = "Impossible to download the data"
        choices = ["Close"]
        reply = buttonbox(msg, image=People.image, choices=choices)
        if reply == "Close":
            sys.exit(1)


# starter
parser()
