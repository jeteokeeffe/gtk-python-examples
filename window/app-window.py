import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

win = Gtk.ApplicationWindow()
    
win.set_title("Gtk.ApplicationWindow Example")
win.set_default_size(500,500)
win.set_position(Gtk.WindowPosition.CENTER)
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
