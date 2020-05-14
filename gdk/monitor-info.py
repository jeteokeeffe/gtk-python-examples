"""
Get Monitor Information
"""

import gi
gi.require_version('Gdk', '3.0')

from gi.repository import Gdk

    # Get Display
display = Gdk.Display.get_default()

    # Find num of monitors
num_monitors = display.get_n_monitors()
print("Monitors found: {}".format(num_monitors))
print()

for i in range(0, num_monitors):
    print("Monitor: {}".format(i))
        # Gdk.Monitor
    monitor = display.get_monitor(i)
    
    print("Model: " + monitor.get_model())
    print("Manufacturer: " + monitor.get_manufacturer())
    print("Refresh: {}Hz".format( monitor.get_refresh_rate() / 1000 ))

    rect = monitor.get_geometry()
    print("Monitor Dimensions: {} {} {} {}".format( rect.x, rect.y, rect.width, rect.height))
    #print("Pixel Layout: {}".format( monitor.get_subpixel_layout()))

