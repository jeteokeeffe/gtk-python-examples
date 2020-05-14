import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Example")
        self.set_size_request(300,300)
        self.connect("destroy", Gtk.main_quit)

            # Create List Box
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html 
        box = Gtk.ListBox()
        box.set_selection_mode(Gtk.SelectionMode.NONE)

            # use the libhandy function to add separators to listbox rows
            # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.list_box_separator_header
        box.set_header_func(Handy.list_box_separator_header)

            # Add some rows
        box.add(self.addrow("Firefox"))
        box.add(self.addrow("Chrome"))
        box.add(self.addrow("Opera"))

            # Add List box to main window
        self.add(box)


    def addrow(self, title):
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/CheckButton.html
        check = Gtk.CheckButton.new()

        row = Handy.ActionRow()
        row.add_prefix(check)
        row.set_title(title)
        return row
        

        

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = MyWindow()
window.show_all()
Gtk.main()
