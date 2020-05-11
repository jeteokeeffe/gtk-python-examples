import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy
Handy.init()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='com.example.title_bar')
        GLib.set_application_name('Title Bar')
        GLib.set_prgname('com.example.title_bar')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_icon_name('com.example.title_bar')

        title_bar = Handy.TitleBar()
        header = Gtk.HeaderBar(title='Title Bar', show_close_button=True)

        title_bar.add(header)
        window.set_titlebar(title_bar)

        label = Gtk.Label(wrap=True)
        label.set_markup('<big>This example shows how to use a libhandy '
                         'title bar to hold a regular header bar.</big>')

        window.add(label)
        window.show_all()


def main(version):

    app = Application()
    return app.run(sys.argv)
