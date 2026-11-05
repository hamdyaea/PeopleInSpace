#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Display publicly reported astronauts in space using Tkinter."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import threading
import tkinter as tk
from tkinter import ttk
from urllib.request import Request, urlopen

# The upstream Open Notify API currently publishes this endpoint over HTTP.
API_URL = "http://api.open-notify.org/astros.json"


def parse_people(payload: dict) -> list[tuple[str, str]]:
    if not isinstance(payload, dict) or payload.get("message") != "success":
        raise ValueError("Invalid response from the astronaut API")
    people = payload.get("people")
    if not isinstance(people, list):
        raise ValueError("Astronaut list is missing")
    result = []
    for person in people:
        if not isinstance(person, dict):
            raise ValueError("Invalid astronaut record")
        name, craft = person.get("name"), person.get("craft")
        if not isinstance(name, str) or not isinstance(craft, str):
            raise ValueError("Invalid astronaut name or spacecraft")
        result.append((name, craft))
    return result


def fetch_people(timeout: float = 12) -> list[tuple[str, str]]:
    request = Request(API_URL, headers={"User-Agent": "PeopleInSpace/2.0"})
    with urlopen(request, timeout=timeout) as response:
        data = response.read(200_000)
    return parse_people(json.loads(data.decode("utf-8")))


class PeopleApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("People in Space — Hamdy Abou El Anein")
        self.geometry("630x490")
        self.minsize(450, 340)
        self.configure(bg="#101827")
        self.status = tk.StringVar(value="Press Refresh to retrieve the latest available data.")
        frame = tk.Frame(self, bg="#101827", padx=22, pady=20)
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text="PEOPLE IN SPACE", bg="#101827", fg="#8bd6c1",
                 font=("DejaVu Sans", 16, "bold")).pack(anchor="w")
        tk.Label(frame, textvariable=self.status, bg="#101827", fg="#d0dbea",
                 wraplength=560).pack(anchor="w", pady=12)
        self.spacecraft = tk.PhotoImage(file=str(Path(__file__).with_name("spacecraft-ui.png")))
        tk.Label(frame, image=self.spacecraft, bg="#101827").pack(anchor="w")
        self.listbox = tk.Listbox(frame, bg="#192a40", fg="white", selectbackground="#335f66",
                                  font=("DejaVu Sans", 11), relief="flat")
        self.listbox.pack(fill="both", expand=True)
        self.button = tk.Button(frame, text="Refresh", command=self.refresh, bg="#7ddcc0",
                                fg="#10211c", relief="flat", padx=20, pady=9)
        self.button.pack(anchor="w", pady=14)
        self.refresh()

    def refresh(self) -> None:
        self.button.config(state="disabled")
        self.status.set("Loading astronaut data…")

        def worker() -> None:
            try:
                people = fetch_people()
                error = None
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                people, error = [], str(exc)

            def display() -> None:
                self.button.config(state="normal")
                if error:
                    self.status.set("Unable to retrieve current data: " + error)
                    return
                self.listbox.delete(0, tk.END)
                for name, craft in people:
                    self.listbox.insert(tk.END, name + "  —  " + craft)
                self.status.set(f"{len(people)} people reported in space (Open Notify).")
            try:
                self.after(0, display)
            except RuntimeError:
                pass
        threading.Thread(target=worker, daemon=True).start()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", action="store_true", help="Print a text-only list")
    args = parser.parse_args()
    if args.text:
        try:
            people = fetch_people()
        except (OSError, ValueError) as exc:
            parser.exit(1, f"Unable to retrieve astronaut data: {exc}\n")
        print(f"People in space: {len(people)}")
        for name, craft in people:
            print(f"{name} — {craft}")
    else:
        PeopleApp().mainloop()


if __name__ == "__main__":
    main()
