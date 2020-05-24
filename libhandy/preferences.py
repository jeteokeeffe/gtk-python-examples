import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/PreferencesWindow.html
window = Handy.PreferencesWindow()
window.set_default_size(500, 500)
#window.set_border_width(10)

    # 
    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/PreferencesGroup.html
group1 = Handy.PreferencesGroup()
group1.set_title("My Group")

box = Gtk.ListBox()

    # 
row1 = Handy.ActionRow()
row1.set_title("Page 1 Stuff")

box.insert(row1, -1)

group1.add(box)

    # New tab page (creates a tab in the header bar)
    #
page1 = Handy.PreferencesPage()
page1.set_title("My Page")
page1.add(group1)


    # New tab page (creates another tab in the header bar)
page2 = Handy.PreferencesPage()
page2.set_title("My Other Page")

group2 = Handy.PreferencesGroup()
group2.set_title("Other Group")

    # Add Group to Page
page2.add(group2)

    # Add Pages to Window
window.add(page1)
window.add(page2)


window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
