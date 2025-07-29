Simple fan control for pi 4 monitoring processor temperature. Default pin header is pin 21, targetting a temperature of 45 degrees C.

Install:
sudo apt-get install -y python3-rpi.gpio

Update fanctrl.service and set $HOME to the repo path

sudo cp fanctrl.service /etc/systemd/system/
sudo systemctl enable fanctrl
sudo systemctl start fanctrl

Must use sudo to run fanCtrl.py!



General git setup:
ssh-keygen -C <email>

nano ~/.ssh/config

Host github.com
	IdentityFile <path to private key>

ssh -T git@github.com

Upload public key to github.com
