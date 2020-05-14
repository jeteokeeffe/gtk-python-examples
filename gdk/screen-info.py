import gi

gi.require_version('Gdk', '3.0')

from gi.repository import Gdk


screen = Gdk.Screen.get_default()
print("screen width: {} height: {}".format(screen.get_width(), screen.get_height()))
