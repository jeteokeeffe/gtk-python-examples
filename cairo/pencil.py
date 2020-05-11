# https://developer.gnome.org/gtk3/stable/ch01s05.html
# Converted from C to Python


import gi
import cairo

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

class App(Gtk.Application):

    def on_activate(self,app):
        win = AppWindow(self)
        win.set_title("Drawing Area")
        win.set_border_width(8)

            # Frame
        frame = Gtk.Frame()
        frame.set_shadow_type(Gtk.ShadowType.IN)
        win.add(frame)

            # Drawing Area
        da = Gtk.DrawingArea()
        da.set_size_request(200,200)

            # 
        da.set_events(Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.POINTER_MOTION_MASK )

            # 
        da.connect("motion-notify-event", self.on_notify)
        da.connect("configure-event", self.on_configure)
        da.connect("button-press-event", self.on_press)
        da.connect("draw", self.on_draw)

        frame.add(da)

        win.show_all()

    def on_notify(self, widget, event):
        if event.state & Gdk.ModifierType.BUTTON1_MASK:
            self.draw_brush(widget, event.x, event.y)


    def on_configure(self, widget, event):
        """
        widget      drawingarea object
        event       
        """
        #if self.surface is not None:
        #    del self.surface
        #    self.surface = None

            # GDK Window
        win = widget.get_window()
        self.surface = win.create_similar_surface(cairo.CONTENT_COLOR, 200, 200)

        ctx = cairo.Context(self.surface)
        ctx.set_source_rgb(1,1,1)
        ctx.paint()

        print("configure")

    def on_press(self, draw, event):
        if event.type & Gdk.EventType.BUTTON_PRESS:
            self.draw_brush(draw, event.x, event.y)


    def on_draw(self, widget, ctx):
        ctx.set_source_surface(self.surface, 0, 0)
        ctx.paint()


    def draw_brush(self, draw, x, y):

        ctx = cairo.Context(self.surface)

        ctx.rectangle(x - 3, y - 3, 6, 6)
        ctx.fill()

        draw.queue_draw_area(x - 3, y - 3, 6, 6)
        print("brush {} {}".format(x, y))



class AppWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="hello", application=app)


app=App()
app.connect("activate", app.on_activate)
app.run(None)

