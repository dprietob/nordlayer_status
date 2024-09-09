# NordLayer Status
This script allows you to add icons in the status tray for NordLayer VPN connection in __Elementary OS__. The following will detail how to configure it to run on system boot.

![](https://i.ibb.co/hXYjFBn/disconnected.png)
![](https://i.ibb.co/rcqZ9yf/disconnected-notification.png)
![](https://i.ibb.co/fMV7zTP/connecting.png)
![](https://i.ibb.co/pKm2gVz/connected-notification.png)
![](https://i.ibb.co/f2rG2JK/connected.png)


## Warning
These steps have been performed only on the __Elementary OS 7.1 Horus__ distribution. I do not know if it could give failures in other Linux distributions.

## Note
This documentation uses ``python`` command to run and compile Python scripts. This command may be different on your system (e.g. ``python3``). You should use whatever command is available to you.

## Configuration
First, you need to install [Wingpanel Ayatana-Compatibility Indicator](https://github.com/Lafydev/wingpanel-indicator-ayatana) on your system if it is not already installed. Then, open the script with any code editor and modify ``line 13`` to indicate the ID of the NordLayer gateway you want to connect to (yes, right now only one gateway is supported and it is not configurable):
```
gateway = 'xxx-YYYYYY'
```

## Installation
Once configured to your liking, you can run the script directly using:
```
python nordlayer_status.py
```
If you don't want to have to run this command every time you boot your system, you can tell your Linux distribution to run it for you. To do this, give it run permissions using this command:
```
chmod +x nordlayer_status.py
```

Next, move the ``nordlayer_status.py`` file to the ``~.local/bin/`` directory on your system (create it if not exists), and then create a ``.desktop`` file inside the ``~.config/autostart/`` directory with the following content:
```
[Desktop Entry]
Name=NordLayer Status
GenericName=NordLayer Status
Comment=NordLayer status tray icon
Exec=/home/user/.local/bin/nordlayer_status.py
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
![](https://i.ibb.co/HrGp82m/autostart.png)

