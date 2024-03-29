import dbus

def notification(text):
    bus = dbus.SessionBus()
    notifications = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')
    interface = dbus.Interface(notifications, 'org.freedesktop.Notifications')
    id = 4856
    timeout = 2500
    interface.Notify('name', 0, 'iconPath', 'Stock Alert', text, [], {"urgency":2}, timeout)