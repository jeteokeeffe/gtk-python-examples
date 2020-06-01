import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


dlg = Gtk.AboutDialog.new()
dlg.set_authors(["Author1"])
dlg.set_comments("Native GTK3 QR Scanner")
dlg.set_documenters(["Documenter1"])
dlg.set_license("MIT")
dlg.set_license_type(Gtk.License.MIT_X11)
#dlg.set_logo()
dlg.set_translator_credits("Bob")
dlg.set_version("1.0.0")
dlg.set_website("https://www.gtk.org/")
dlg.set_program_name("About Dialog Example")
dlg.run()
dlg.destroy()
