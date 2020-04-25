import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/IconTheme.html#Gtk.IconTheme.get_default
theme = Gtk.IconTheme.get_default()

    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/IconTheme.html#Gtk.IconTheme.list_icons
for icon in theme.list_icons(None):  # None as context lists all icons
    print(icon)
