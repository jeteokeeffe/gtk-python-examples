import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class MyWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(6)
        self.set_size_request(300, 300)


        headerbar = Gtk.HeaderBar.new()
        headerbar.set_title("Headerbar + Revealer")
        headerbar.set_show_close_button(True)

            # Revealer (allows headerbar to disappear)
        self.revealer = Gtk.Revealer.new()
        self.revealer.add(headerbar)
        self.revealer.set_reveal_child(True)
        self.revealer.set_transition_duration(400)
        self.revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_UP)



            # Switcher Button
        switch = Gtk.Switch.new()
        #switch.valign()
        switch.connect('notify::active', self.on_activate)

            # Add to Window
        self.set_titlebar(self.revealer)
        self.add(switch)
        self.show_all()


    def on_activate(self, widget, ev):
        if widget.get_state() == True:
            self.revealer.set_reveal_child(True)
        else:
            self.revealer.set_reveal_child(False)


win=MyWin()
win.connect('destroy', Gtk.main_quit)
Gtk.main()
