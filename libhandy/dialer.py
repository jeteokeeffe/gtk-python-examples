"""
https://lazka.github.io/pgi-docs/#Handy-0.0
"""

import gi
import sys

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy


def print_number(dialer, number):
    print("Dial {}".format(number))


def quit(dialer, number=None):
    Gtk.main_quit()


    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = Gtk.Window(title="Dialer Example with Python")
window.set_border_width(10)

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/Dialer.html
dialer = Handy.Dialer()

dialer.connect("submitted", print_number)
dialer.connect("submitted", quit)
window.add(dialer)

window.show_all()
Gtk.main()

