# NordLayer Status
This script allows you to add icons in the status tray for NordLayer VPN connection in __Elementary OS__. The following will detail how to configure it to run on system boot.

![](https://i.ibb.co/zHrhHTr/screenshot.png)

## Warning
These steps have been performed only on the __Elementary OS 7.1 Horus__ distribution. I do not know if it could give failures in other Linux distributions.

## Note
This documentation uses ``python`` command to run and compile Python scripts. This command may be different on your system (e.g. ``python3``). You should use whatever command is available to you.

## Configuration
First of all, it's necessary install [Wingpanel Ayatana-Compatibility Indicator](https://github.com/Lafydev/wingpanel-indicator-ayatana) on your system if it is not already installed. Afterwards, you can open the script with any code editor and modify it to add options according to your needs. The script is very short and simple and includes some commented features by default, so it will not be difficult for you to understand how it works.

## Installation
Once configured to your liking, you can run the script directly using:
```
python vpn-indicator.py
```
If you don't want to have to run this command every time you boot your system, you can tell your Linux distribution to run it for you. To do this, give it run permissions using this command:
```
chmod +x vpn-indicator.py
```

Next, move the ``vpn-indicator.py`` file to the ``~.local/bin/`` directory on your system (create it if not exists), and then create a ``.desktop`` file inside the ``~.config/autostart/`` directory with the following content:
```
[Desktop Entry]
Name=NordLayer Status
GenericName=NordLayer Status
Comment=NordLayer status tray icon
Exec=nordlayer_status.py
Terminal=false
Type=Application
Icon=nordlayer-icon-path
Categories=Utility;
Keywords=shorcut;app;
StartupNotify=false
X-GNOME-Autostart-enabled=true
```
Obviously, all sections must be configured according to your needs.

This should make the application recognized by the system and available to start at system boot.
![](https://i.ibb.co/rkMN5Hd/system-boot.png)

