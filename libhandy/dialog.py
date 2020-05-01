"""
https://lazka.github.io/pgi-docs/#Handy-0.0
"""

import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy



    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = Gtk.Window(title="LibHandy Dialog Example")
window.set_border_width(10)
window.set_default_size(400, 400)

    # https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Label.html
label = Gtk.Label.new("This your mobile friendly dialog")

    
    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/Dialog.html
dialog = Handy.Dialog.new(window)
box = dialog.get_content_area()
box.add(label)
dialog.show_all()


window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
