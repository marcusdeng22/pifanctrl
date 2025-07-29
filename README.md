Simple fan control for pi 4 monitoring processor temperature. Default pin header is pin 21, targetting a temperature of 45 degrees C.

Install:
sudo apt-get install -y python3-rpi.gpio

update fanctrl.service and set $HOME to the repo path

sudo cp fanctrl.service /etc/systemd/system/
sudo systemctl enable fanctrl
sudo systemctl start fanctrl

Must use sudo to run fanCtrl.py!
