#!/usr/bin/env python
import sys

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk

w = Gtk.Window()

screen = Gdk.Screen.get_default()
print ("Montors: %d" % screen.get_n_monitors())
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 0

l = Gtk.Button(label="Hello, %d monitors!" % screen.get_n_monitors())
w.add(l)
w.show_all()

w.fullscreen_on_monitor(screen, n)
l.connect("clicked", Gtk.main_quit)
w.connect("destroy", Gtk.main_quit)
Gtk.main()
