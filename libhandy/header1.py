import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy, Gio

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = Gtk.Window(title="LibHandy Headerbar")
window.set_default_size(400, 200)
window.set_border_width(10)


    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/HeaderBar.html
header = Handy.HeaderBar()
header.set_title("hello")
header.set_subtitle("how to use libhandy headerbar")
header.set_show_close_button(True)

    # Override default titlebar
window.set_titlebar(header)


button = Gtk.Button.new()
icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
button.add(image)
header.pack_end(button)

    #
box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
Gtk.StyleContext.add_class(box.get_style_context(), "linked")

button = Gtk.Button()
button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
box.add(button)

button = Gtk.Button()
button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
box.add(button)

header.pack_start(box)

    # Add Text View for show something
window.add(Gtk.TextView())

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
