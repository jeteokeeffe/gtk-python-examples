import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

    # First Button
    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Button.html
btn1 = Gtk.Button()
btn1.set_label("First Button")

    # Second Button
    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Button.html
btn2 = Gtk.Button.new_with_label("Button with CSS")

    # Common: destructive-action, warning-action, suggested-action
    #
    # https://wiki.gnome.org/HowDoI/Buttons
    # https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Widget.html#Gtk.Widget.get_style_context
btn2.get_style_context().add_class("suggested-action")

    # 3rd Button
btn3 = Gtk.Button.new_from_icon_name("process-stop", Gtk.IconSize.BUTTON)
btn3.set_label("Label and Icon")
btn3.set_always_show_image(True)
   
    # 4th Button - Icon only
btn4 = Gtk.Button.new_from_icon_name("process-stop", Gtk.IconSize.BUTTON)

    # Switch
switch1 = Gtk.Switch()
switch1.set_active(False)

    # Switch
switch2 = Gtk.Switch()
switch2.set_active(False)

    # Check Button
chkbtn1 = Gtk.CheckButton()

    # Check Button
chkbtn2 = Gtk.CheckButton()
chkbtn2.set_label("Checkbox with Label")

    # Link Button
link1 = Gtk.LinkButton.new("https://www.gtk.org/")

    # Link Button
link2 = Gtk.LinkButton.new_with_label("https://www.gtk.org/", "GTK Website")

    
listbox = Gtk.ListBox()
listbox.set_selection_mode(Gtk.SelectionMode.NONE)
listbox.insert(btn1, -1)
listbox.insert(btn2, -1)
listbox.insert(btn3, -1)
listbox.insert(btn4, -1)
listbox.insert(switch1, -1)
listbox.insert(switch2, -1)
listbox.insert(chkbtn1, -1)
listbox.insert(chkbtn2, -1)
listbox.insert(link1, -1)
listbox.insert(link2, -1)

win = Gtk.Window()
win.set_border_width(10)
win.set_title("Buttons")
win.add(listbox)

win.show_all()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
