"""
A single page with a single group using LibHandy's Preference window
"""
import gi

gi.require_version('Handy', '0.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Handy

    # https://lazka.github.io/pgi-docs/#Handy-0.0/functions.html#Handy.init 
Handy.init()

    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/PreferencesWindow.html
window = Handy.PreferencesWindow()

    # Create a page (tab)
    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/PreferencesPage.html
page1 = Handy.PreferencesPage()
page1.set_title("Folder Settings")
page1.set_icon_name("folder")


    # Create a Group (our first group)
    # https://lazka.github.io/pgi-docs/#Handy-0.0/classes/PreferencesGroup.html
browsegroup = Handy.PreferencesGroup()
browsegroup.set_title("Browsing")

    # Create List Box (specifically for browsing group)
browsebox = Gtk.ListBox()
browsebox.set_selection_mode(Gtk.SelectionMode.NONE)

    # Create a Toggle Button
switch = Gtk.Switch()
switch.set_active(True)

    # Create a Row
row1 = Handy.ActionRow()
row1.set_title("Enable Smooth Scaling")
row1.add_action(switch)

    # Add Some Rows to the Box
    # pos = -1 means add to end of list
browsebox.insert(row1, -1)

    # Add List box to group
browsegroup.add(browsebox)


    # Add Groups to Page
page1.add(browsegroup)

    # Add Page to Window
window.add(page1)

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

