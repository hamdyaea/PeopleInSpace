# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("app", Path(__file__).resolve().parents[1] / "PeopleSpace.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class Tests(TestCase):
    def test_parse(self):
        data = {"message": "success", "people": [{"name": "A", "craft": "ISS"}]}
        self.assertEqual(app.parse_people(data), [("A", "ISS")])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            app.parse_people({"message": "error"})

    def test_gui(self):
        with patch.object(app.PeopleApp, "refresh"):
            window = app.PeopleApp()
            try:
                self.assertIn("PEOPLE IN SPACE", window.winfo_children()[0].winfo_children()[0].cget("text"))
            finally:
                window.destroy()
