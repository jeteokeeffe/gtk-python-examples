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

    def on_notify(self, event, data):

        print("notify")

    def on_configure(self, event, data):
        #self.surface = Gdk.Window()
        print("configure")

    def on_press(self, draw, event):
        if event.type & Gdk.EventType.BUTTON_PRESS:
            self.draw_brush(draw, event.x, event.y)


    def on_draw(self, widget, ctx):
        print("draw")


    def draw_brush(self, draw, x, y):

        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 200)
        ctx = cairo.Context(surface)

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

