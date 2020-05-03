#!/usr/bin/python

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__()


    def on_key_press(self, widget, event):
        print("")



win = MyWindow()
win.show_all()
Gtk.main()
