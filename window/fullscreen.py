import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = Gtk.Label.new("Hello World")
        self.add(label)


class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.myapp", **kwargs)
        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = AppWindow(application=self, title="Main Window")
        self.window.fullscreen()
        self.window.present()
        self.window.show_all()


app = Application()
app.run(sys.argv)
