#!/usr/bin/python
#
# 

import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify

    # https://lazka.github.io/pgi-docs/Notify-0.7/functions.html
Notify.init("Your App Name")

    # https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html
Hello = Notify.Notification.new("Hello world", "This is an example notification.", "dialog-information")

    # https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html#Notify.Notification.show
Hello.show()

