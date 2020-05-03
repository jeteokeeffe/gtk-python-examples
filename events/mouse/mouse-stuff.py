
import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class EventsTest(Gtk.Grid):
    def __init__(self):
        super(EventsTest, self).__init__()

        btn = Gtk.Button("Top right")
        btn.connect("clicked", lambda x: print("Button clicked"))

        self.attach(Gtk.Label("Top left"), 0, 0, 1, 1)
        self.attach(btn, 1, 0, 1, 1)
        self.attach(Gtk.SpinButton(), 0, 1, 1, 1)


class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect("destroy", lambda x: Gtk.main_quit())
        self.connect("button-press-event", self.on_button_pressed)
        self.connect("event-after", self.on_event_after)

        evtest = EventsTest()

        self.add(evtest)
        self.show_all()

    def on_button_pressed(self, btn, event):
        print("Main window button pressed")
        return True

    def on_event_after(self, wdg, event):
        print("Event after")

    def run(self):
        Gtk.main()


def main(args):
    mainwdw = MainWindow()
    mainwdw.run()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
