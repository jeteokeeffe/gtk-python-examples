import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy


class MyWindow(Gtk.Window):

    def __init__(self):

            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Window.html
        Gtk.Window.__init__(self)

        self.set_title("Example")
        self.connect("destroy", Gtk.main_quit)

            # Create List Box
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html 
        box = Gtk.ListBox()
        box.set_selection_mode(Gtk.SelectionMode.NONE)

            # use the libhandy function to add separators to listbox rows
            # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.list_box_separator_header
        box.set_header_func(Handy.list_box_separator_header)

            # Add some rows
        box.add(self.addrow())

            # Add List box to main window
        self.add(box)


    def addrow(self, title):

        row = Handy.ActionRow()
        return row


    def addseparatorcallback(self, row, before):
            # First row, dont add separator
        if before == None:
            return

        if not row == None:
                # https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Orientation
            row.set_header(Gtk.Separator.new(Gtk.Orientation.HORIZONTAL))


    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = MyWindow()
window.show_all()
Gtk.main()
