import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


window = Gtk.Window()
window.set_default_size(400, 400)

headerbar = Gtk.HeaderBar()

window.set_titlebar(headerbar)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
