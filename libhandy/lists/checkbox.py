import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Example")
        self.connect("destroy", Gtk.main_quit)

            # Create List Box
            # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html 
        box = Gtk.ListBox()
        box.set_selection_mode(Gtk.SelectionMode.NONE)
        box.set_header_func(self.addseparatorcallback)

            # Add some rows
        box.add(self.addrow( "Firefox"))
        box.add(self.addrow( "Chrome"))
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
        

    def addseparatorcallback(self, row, before):
            # First row, dont add separator
        if before == None:
            return

        if not row == None:
                # https://lazka.github.io/pgi-docs/Gtk-3.0/enums.html#Gtk.Orientation
            row.set_header(Gtk.Separator.new(Gtk.Orientation.HORIZONTAL))
        

window = MyWindow()
window.show_all()
Gtk.main()
