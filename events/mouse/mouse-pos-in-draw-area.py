import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')

from gi.repository import Gdk, Gtk, GObject

class Ventana(Gtk.Window):

    def __init__(self):
        super(Ventana, self).__init__()

        self.set_title('Test')
        self.set_size_request(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect('destroy', Gtk.main_quit)

        drawing_area = Gtk.DrawingArea()
        drawing_area.set_size_request(780, 500)
        drawing_area.connect('button-press-event', self.on_drawing_area_button_press)
        drawing_area.connect('draw', self.on_draw)
        drawing_area.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)

        fixed = Gtk.Fixed()
        fixed.put(drawing_area, 10, 10)

        self.add(fixed)

        self.show_all()

    def on_drawing_area_button_press(self, widget, event):
        print(event.x, ' ', event.y)

    def on_draw(self, widget, context):
        color = Gdk.RGBA(.5,.5,.5,.5)
        #widget.modify_bg(Gtk.StateType.NORMAL, color)
        widget.override_background_color(Gtk.StateType.NORMAL, color)
        context.paint()
        
        print("hello")


    

win = Ventana()
Gtk.main()
