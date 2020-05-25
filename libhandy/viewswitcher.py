import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

    # Setup HeaderBar
header = Handy.HeaderBar.new()
header.set_show_close_button(True)

window = Gtk.Window(title="ViewSwitcher Example")
window.set_border_width(10)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

stack = Gtk.Stack.new()
stack.add_titled(Gtk.Label.new("Outstanding"), "outstanding", "Outstanding")
stack.add_titled(Gtk.Label.new("Completed"), "completed", "Completed")

vbox.pack_start(stack, True, True, 0)

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/ViewSwitcher.html
switcher = Handy.ViewSwitcher.new()
switcher.set_stack(stack)

    # Add centered widget
header.set_custom_title(switcher)

    # Add header bar
window.set_titlebar(header)

window.add(vbox)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
