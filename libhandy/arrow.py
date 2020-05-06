"""
Handy.Arrows seems to be deprecated
"""

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Handy', '0.0')

from gi.repository import Gtk, Handy


Handy.init()

seconds = 3

win = Gtk.Window()
win.set_title("Arrows Example")
win.set_border_width(10)

arrow = Handy.Arrows.new()
arrow.set_direction(Handy.ArrowsDirection.UP)
arrow.set_count(3)
arrow.set_duration(seconds * 1000)

win.add(arrow)


win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
