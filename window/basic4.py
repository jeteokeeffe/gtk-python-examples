import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.set_title("My First Window Example")
win.show()
Gtk.main()
