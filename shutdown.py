"""
#!/usr/bin/env python
#title           :shutdown.py
#description     :Python Script read Raspberry Pi GPIO pin (digital input)
#author          :Achmad Syahrul Irwansyah
#date            :2023/03/30
#version         :0.1
#usage           :Python
#notes           :
#python_version  :2.7.17
#==============================================================================
"""

import sys
import time
import RPi.GPIO as GPIO
import subprocess as run

PASSWORD = sys.argv[1]

GPIO_PIN_S = 27
GPIO_PIN_A = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN_S, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GPIO_PIN_A, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.5)
    if GPIO.input(GPIO_PIN_A) == GPIO.LOW:
        if GPIO.input(GPIO_PIN_S) == GPIO.HIGH:
            print("Shutdown!!")
            run.call("echo '" + PASSWORD + "' | sudo -S shutdown -h now", shell=True)
            #run.call("echo '" + PASSWORD + "' | sudo -S shutdown -r now", shell=True)
        else:
            print("System Power ON.")
    else:
        print("Connect the wire!")
