#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Compatibility CLI for the People in Space application."""
from PeopleSpace import main

if __name__ == "__main__":
    import sys
    sys.argv = [sys.argv[0], "--text"]
    main()
