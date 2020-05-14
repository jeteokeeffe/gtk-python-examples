import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy, Gio


class MyWindow(Gtk.Window):

    def __init__(self):

            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Window.html
        Gtk.Window.__init__(self)

        self.set_title("Favorite Browser")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)
        self.set_size_request(350,350)

        mystyle = "#myround { border-radius: 20px; }"
        provider = Gtk.CssProvider.new()
        provider.load_from_file(Gio.File.new_for_path("radio.css"))

            # Create List Box
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html 
        box = Gtk.ListBox()
            # Important to map css
        box.set_name("myround")
        style = box.get_style_context()
        style.add_provider(provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
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
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/RadioButton.html
        radio = Gtk.RadioButton.new()

        row = Handy.ActionRow()
        row.add_prefix(radio)
        row.set_title(title)

        return row




    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

window = MyWindow()
window.show_all()
Gtk.main()
