# pyshutdown
Python code to shutdown reComputer-J202 Nvidia Jetson Development Module using GPIO signal input. This code using `gpiod` v1.5.3 python library.

# Installation
1. Clone this git into your home directory
```bash
cd
git clone https://github.com/syahrulirwansyah12/pyshutdown.git -b reComputer-J202
```
2. Install python dependencies. If you are using pip package manager, you can run
```bash
pip install gpiod os-sys subprocess.run time
```
4. Add the python code to crontab. Run the crontab editor
```bash
crontab -e
```
Then add this line
```bash
@reboot python /home/<user>/pyshutdown/shutdown.py
```
Replace `<user>` with your username.
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
1. Connect header pin 7 to 3.3V (header pin 1) with 2.2k ohm resistor. Then, connect header pin 7 to GND (header pin 9) with a switch.
2. Connect header pin 18 to GND (header pin 20) to ACTIVATE the auto-shutdown.
3. Connect header pin 18 to 3.3V (header pin 17) to DEACTIVATE the auto-shutdown and use the reComputer-J202 normally.

!!! If you don't connect header pin 18 to 3.3V nor GND the value will be floating and causing the reComputer-J202 to not work properly !!!
