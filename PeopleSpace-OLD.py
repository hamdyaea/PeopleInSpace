#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
#
# hamdy.aea@protonmail.com
#
# This Python 3 software show in real-time how many people are in space.
# Created with the api of http://open-notify.org/Open-Notify-API/People-In-Space/

from easygui import *
import wget
import json
import os
import sys

name = ""
spacecraft = ""
total = ""


def parser():
    global name, spacecraft, total
    with open("rawdata", "r") as f:
        people = json.load(f)
        if people["message"] == "success":
            key = (people["number"]) - 1
            keyload = 0
            while keyload <= key:
                displaykey = key + 1
                name = name + (
                    ("Name of the astronaut : ")
                    + str(people["people"][keyload]["name"])
                    + str("\n\n")
                    + str("Spacecraft : ")
                    + str(people["people"][keyload]["craft"])
                    + str("\n\n")
                )
                keyload = keyload + 1
                if keyload > key:
                    break
            image = "spacecraft.gif"
            msg = (
                ("This software show in real-time how many people are in space.\n\n")
                + str(("Number of people in space : ") + str(people["number"]))
                + str("\n\n")
                + (name)
            )
            choices = ["Close"]
            reply = buttonbox(msg, image=image, choices=choices)
            if reply == "Close":
                sys.exit(0)
            else:
                msg = "Impossible to download the data"
                choices = ["Close"]
                reply = buttonbox(msg, image=image, choices=choices)
                if reply == "Close":
                    sys.exit(1)



filePath = "rawdata"

if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("")

url = "http://api.open-notify.org/astros.json"
filename = wget.download(url, out="rawdata")


parser()
