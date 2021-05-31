#!/usr/bin/env python3

import urllib.request, json
with urllib.request.urlopen("http://api.open-notify.org/astros.json") as url:
    data = json.loads(url.read().decode())

    howmany = data["number"]
    wholist = data["people"]

    print(str("Total People in space : ")+str(howmany))
    print("\n")
    for i in wholist:
        print(str("Name : ")+str(i["name"]))
        print(str("Spacecraft : ")+str(i["craft"]))
        print("\n")
