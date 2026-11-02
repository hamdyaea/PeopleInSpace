# People in Space

A lightweight Python 3 + Tkinter viewer for the public Open Notify astronaut roster.

**Developer:** Hamdy Abou El Anein
**Contact:** info@daylightlinux.ch
**License:** GNU GPL v3 (see LICENSE).

## Features

- Modern Tkinter interface replacing EasyGUI.
- Asynchronous refresh so the interface stays responsive.
- Input validation, timeout handling and explicit error messages.
- Text-only mode for terminals and scripts.

## Data limitations

Open Notify may be unavailable or delayed; its astronaut roster should not be
treated as an authoritative real-time mission manifest. Its original API endpoint
is served over HTTP rather than HTTPS. The application does not collect user data.

## Run

    python3 PeopleSpace.py
    python3 PeopleSpace.py --text

## Test

    python3 -m unittest discover -s tests -v

Original source: [old branch](https://github.com/hamdyaea/PeopleInSpace/tree/old).
