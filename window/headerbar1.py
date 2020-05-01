import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


window = Gtk.Window()
window.set_default_size(400, 400)
window.set_border_width(10)


headerbar = Gtk.HeaderBar()
headerbar.set_title("Headerbar Example")
headerbar.set_subtitle("Hello")
headerbar.set_decoration_layout('menu:minimize,maximize,close')
headerbar.set_show_close_button(True)

button = Gtk.Button.new_from_icon_name('list-add-symbolic.symbolic', Gtk.IconSize.SMALL_TOOLBAR )
headerbar.pack_start(button)


window.set_titlebar(headerbar)
window.add(Gtk.TextView())

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
