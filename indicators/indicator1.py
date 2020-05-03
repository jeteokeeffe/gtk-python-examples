import os
import gi

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk, AppIndicator3

def main():
        # https://lazka.github.io/pgi-docs/AppIndicator3-0.1/classes/Indicator.html
    indicator = AppIndicator3.Indicator.new("customtray", "semi-starred-symbolic", AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    menu = Gtk.Menu()

        # https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html#Gtk.MenuItem
    commanditem = Gtk.MenuItem.new()
    commanditem.set_label('My notes')
    commanditem.connect('activate', notes)
    menu.append(commanditem)
    

    exititem = Gtk.MenuItem.new()
    exititem.set_label('exit')
    exititem.connect('activate', quit)
    menu.append(exititem)

    menu.show_all()

    indicator.set_menu(menu)
    Gtk.main()


def notes(_):
    os.system("gedit $HOME/Documents/Notes.txt")

def quit(_):
    Gtk.main_quit()



main()
