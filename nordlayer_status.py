#!/usr/bin/env python3
import gi
import subprocess
import threading
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')
gi.require_version('GLib', '2.0')
gi.require_version('Notify', '0.7')
from gi.repository import GLib, Gtk, AppIndicator3, Notify

def main():
    global gateway
    gateway = 'xxx-YYYYYY'
    update_icon(last_status)
    update_menu(last_status)

    GLib.timeout_add(2000, update)
    Gtk.main()

def update():
    global last_status
    current_status = is_vpn_active()

    if current_status != last_status:
        update_icon(current_status)
        update_menu(current_status)
        show_toast(current_status)
        last_status = current_status
    return True

def update_icon(is_active):
    if is_active:
        indicator.set_icon_full("security-high", "VPN Connected")
    else:
        indicator.set_icon_full("security-medium", "VPN Disconnected")

def update_menu(is_active):
    menu = Gtk.Menu()

    if is_active:
        # Status option
        status = Gtk.MenuItem(label="Connected to " + gateway)
        status.set_sensitive(False)
        menu.append(status)

        menu.append(Gtk.SeparatorMenuItem())

        # Disconnect option
        disconnect = Gtk.MenuItem(label="Disconnect VPN")
        disconnect.connect("activate", disconnect_vpn)
        menu.append(disconnect)
    else:
        # Status option
        status = Gtk.MenuItem(label="VPN disconnected")
        status.set_sensitive(False)
        menu.append(status)

        menu.append(Gtk.SeparatorMenuItem())

        # Connect option
        connect = Gtk.MenuItem(label="Connect VPN")
        connect.connect("activate", connect_vpn)
        menu.append(connect)

    menu.show_all()
    indicator.set_menu(menu)

def show_toast(is_active):
    if is_active:
        show_notification('VPN connection', 'Connected to NordLayer gateway ' + gateway, 'security-high')
    else:
        show_notification('VPN connection', 'VPN disconnected', 'security-medium')

def is_vpn_active():
    result = subprocess.run(['nordlayer', 'status'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return "VPN: Connected" in output

def disconnect_vpn(menu_item):
    threading.Thread(target=run_command, args=(['nordlayer', 'disconnect'],)).start()

def connect_vpn(menu_item):
    show_notification('VPN connection', 'Connecting VPN...', 'security-low')
    threading.Thread(target=run_command, args=(['nordlayer', 'connect', gateway],)).start()

def run_command(command):
    subprocess.run(command, stdout=subprocess.PIPE)

def show_notification(title, message, icon):
    Notify.init("NordLayer Tray")
    notification = Notify.Notification.new(title, message, icon)
    notification.show()

if __name__ == "__main__":
    global indicator, last_status, gateway
    indicator = AppIndicator3.Indicator.new("vpntray2", "security-medium", AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
    last_status = False
    main()
