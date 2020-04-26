#!/usr/bin/python
#
# https://www.devdungeon.com/content/desktop-notifications-linux-python

import os
import gi

gi.require_version('Notify', '0.7')

from gi.repository import Notify

def backup():
    os.system("/usr/bin/gedit")
    print("clicked action")


    # https://lazka.github.io/pgi-docs/Notify-0.7/functions.html
Notify.init("App Name")

    # Create the notification object
summary = "Backing up!"
body = "Meeting at 3PM!"
icon = os.path.abspath("backup.png")

    # https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html
notification = Notify.Notification.new(summary, body, icon)


    # https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html#Notify.Notification.add_action
notification.add_action(
    "action_click",
    "Open Gedit",
    backup,
    None # Arguments
)

    # Must be after add_action to ensure the action is set
    # https://lazka.github.io/pgi-docs/Notify-0.7/classes/Notification.html#Notify.Notification.show
notification.show()

    # 
Notify.uninit()
