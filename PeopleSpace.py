#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com


import json
from easygui import *
import sys
import urllib.request  # install it with : pip3 install urllib3

total = ""
name = ""
space_name = ""
space_craft = ""
image = "spacecraft.gif"


def parser():
    global name, space_name, space_craft, total
    urlData = "http://api.open-notify.org/astros.json"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset("utf-8")
    space = json.loads(data.decode(encoding))
    total = space["number"]
    if space["message"] == "success":
        for i in space["people"]:
            space_name = i["name"]
            space_craft = i["craft"]
            name = name + (
                ("Name of the astronaut : ")
                + str(space_name)
                + str("\n\n")
                + str("Spacecraft : ")
                + str(space_craft)
                + str("\n\n")
            )

        msg = (
            ("This software show in real-time how many people are in space.\n\n")
            + str("Number of people in space : ")
            + str(total)
            + str("\n\n")
            + (name)
        )
        choices = ["Close"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Close":
            sys.exit(0)
        else:
            sys.exit(0)

    else:
        print("no data - error")


parser()
