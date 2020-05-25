import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = Gtk.Window(title="ViewSwitcher Example")
window.set_border_width(10)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/ViewSwitcher.html
switcher = Handy.ViewSwitcher.new()
switcher.set_stack()

stack = Gtk.Stack.new()

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/ViewSwitcherBar.html
bar = Handy.ViewSwitcherBar.new()
bar.set_stack(stack)

vbox.pack_start(bar, True, True, 0)

window.add(vbox)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
