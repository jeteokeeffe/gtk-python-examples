import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
    # Width = 400, Height = 200
win.set_default_size(400, 200)
win.set_title("Set Window Size Example")
win.show()
Gtk.main()
