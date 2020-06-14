import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk


down = Gtk.DropDown.new()
down.set_from_strings()
down.set_selected()
down.set_factory()
down.set_set_list_factory()
down.set_expression()
down.set_enable_search(False)

