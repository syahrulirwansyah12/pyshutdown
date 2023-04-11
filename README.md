# pyshutdown
Python code to shutdown Raspberry Pi using GPIO signal input. This code uses `RPi.GPIO` python library and works well in Raspberry Pi 3 Model B+.

# Installation
1. Clone this git into your home directory
```bash
cd
git clone https://github.com/syahrulirwansyah12/pyshutdown.git -b Raspberry-Pi
```
2. Install python dependencies. If you are using pip package manager, you can run
```bash
pip install RPi.GPIO subprocess.run time
```
4. Add the python code to crontab. Run the crontab editor
```bash
crontab -e
```
Then add this line
```bash
@reboot python /home/<user>/pyshutdown/shutdown.py <user-password>
```
Replace `<user>` with your username and `<user-password>` with your user password.

5. Save and exit the crontab editor
6. Reboot your Ubuntu machine
```bash
sudo reboot
```
7. You can check whether the program is running or not by running
```bash
sudo systemctl status cron
```
or
```bash
ps -ef | grep python
```
This will show all running Python processes.

# GPIO Pin Used (Default)
1. Connect `GPIO Pin 27` (header pin 13) to `GND` (header pin 14) with a switch.
2. Connect `GPIO Pin 17` (header pin 11) to `GND` (header pin 9) to ACTIVATE the `auto-shutdown`. 
3. Or disconnect `GPIO Pin 17` (header pin 11) from `GND` (header pin 9) to DEACTIVATE the `auto-shutdown` and use the Raspberry-Pi normally.

If you ACTIVATE the `auto-shutdown` feature, you have to close (connect) the switch so that `GPIO Pin 27` is connected to `GND` to Power-ON your Raspberry-Pi. If you open (disconnect) the switch, the Raspberry-Pi will shutdown automatically and you can wait until it completely shutdown before unplug the power line.
