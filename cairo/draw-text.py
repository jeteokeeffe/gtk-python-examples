import gi
import cairo

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("GTK window")
        self.resize(420, 120)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, widget, cr):

            # What Color the text should be
        cr.set_source_rgb(255, 0, 0)
            # Type of font
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
            # font size
        cr.set_font_size(40)
        
            # Where to draw on screen
        cr.move_to(10, 50)
            # What text to write
        cr.show_text("Draw Text Example.")

        cr.set_source_rgb(255, 0, 255)

        cr.move_to(50, 30)

        cr.show_text("Another Example")
        
    
app = Example()
Gtk.main()
