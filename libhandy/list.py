import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy, Gio, GObject

class Flatpak(GObject.GObject):
    name = GObject.Property(type=str)
    repo = GObject.Property(type=str)

    def __init__(self, name, repo):
        GObject.GObject.__init__(self)
        self.name = name
        self.repo = repo


def button_clicked(btn):
    print("button clicked")

def bind_model_func(flatpak):
    print(flatpak.name)
    return flatpak.name

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

    # Create Window
window = Gtk.Window(title="LibHandy List example")
window.set_border_width(10)

    # Create a Button
    #
button = Gtk.Button.new_from_icon_name('battery-good', Gtk.IconSize.MENU )
button.connect("clicked", button_clicked)

    # Build Action Row
    # 
row1 = Handy.ActionRow()
row1.set_icon_name('firefox-symbolic')
row1.set_title("Action Row")
row1.set_subtitle("this is a subtitle")
row1.add_action(button)


    # Create List Store
store = Gio.ListStore()
store.append(Flatpak("flatseal", "flathub"))
store.append(Flatpak("music", "flathub"))


    # Build Combo Row
    # 
row2 = Handy.ComboRow()
row2.set_icon_name('face-wink')
row2.set_title("Combo Row")
row2.set_subtitle("this is a subtitle")
row2.bind_name_model(store, bind_model_func)

label = Gtk.Label.new("This is shown when expanded. This is hidden when not expanded")

    # Build Expandable Row
    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/ExpanderRow.html
row3 = Handy.ExpanderRow()
row3.set_icon_name('battery-good')
row3.set_title("Expander Row")
row3.set_subtitle("this is a subtitle")
row3.set_expanded(False)
row3.set_show_enable_switch(False)
row3.add(label)
row3.show_all()

    # Create List Box
    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html 
box = Gtk.ListBox()
box.set_selection_mode(Gtk.SelectionMode.NONE)

    # Add Rows to List Box
    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html#Gtk.ListBox.insert
box.insert(row1, -1)
box.insert(row2, -1)
box.insert(row3, -1)

    # Add List Box
window.add(box)
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
