import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class StackWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)


        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)


            # Stack
        stack = Gtk.Stack()

            # Stack Effects
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

            # Stack #1
        checkbutton = Gtk.CheckButton.new_with_label("Click me!")
        stack.add_titled(checkbutton, "check", "Check Button")

            # Stack #2
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "A label")

            # Create Switcher
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)

            #  Add Stack to Main Vertical Box
        vbox.pack_start(stack, True, True, 0)

        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.set_custom_title(stack_switcher)

        self.set_titlebar(header)


win = StackWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
