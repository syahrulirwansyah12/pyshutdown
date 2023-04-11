#!/usr/bin/env python

import time
import sys
import subprocess as run #library for running command in shell

sys.path.append('/usr/lib/python3/dist-packages')

import gpiod as GPIO #library for linux GPIO

# Enter your password
PASSWORD = sys.argv[1]

# Header pin constant
HEADER_PIN_7 = 'PS.04' #Used for shutdown
HEADER_PIN_8 = 'PR.02'
HEADER_PIN_10 = 'PR.03'
HEADER_PIN_11 = 'PR.04'
HEADER_PIN_12 = 'PT.05'
HEADER_PIN_13 = 'PY.00'
HEADER_PIN_15 = 'PCC.00'
HEADER_PIN_16 = 'PY.04'
HEADER_PIN_18 = 'PY.03' #Used for shutdown
HEADER_PIN_19 = 'PZ.05'
HEADER_PIN_21 = 'PZ.04'
HEADER_PIN_22 = 'PY.01'
HEADER_PIN_23 = 'PZ.03'
HEADER_PIN_24 = 'PZ.06'
HEADER_PIN_26 = 'PZ.07'
HEADER_PIN_27 = 'PDD.00'
HEADER_PIN_28 = 'PCC.07'
HEADER_PIN_29 = 'PQ.05'
HEADER_PIN_31 = 'PQ.06'
HEADER_PIN_32 = 'PR.00'
HEADER_PIN_33 = 'PN.01'
HEADER_PIN_35 = 'PU.00'
HEADER_PIN_36 = 'PR.05'
HEADER_PIN_37 = 'PY.02'
HEADER_PIN_38 = 'PT.07'
HEADER_PIN_40 = 'PT.06'

# Consumer
CONSUMER = 'gpio_shutdown'

# Chip variables
chip0 = None
chip1 = None
chip2 = None

# Open chip function
def open_chip():
    global chip0, chip1, chip2
    
    #chip0 = GPIO.chip('/dev/gpiochip0', GPIO.chip.OPEN_BY_PATH)
    chip1 = GPIO.chip('/dev/gpiochip1', GPIO.chip.OPEN_BY_PATH)
    chip2 = GPIO.chip('/dev/gpiochip2', GPIO.chip.OPEN_BY_PATH)

# Pin configuration function for input
def pin_config_input(gpio_pin):
    gpio_pin_config = GPIO.line_request()
    gpio_pin_config.consumer = CONSUMER
    gpio_pin_config.request_type = GPIO.line_request.DIRECTION_INPUT
    gpio_pin.request(gpio_pin_config)

# Open GPIO chip
try:
    open_chip()
except:
    run.call("echo '" + PASSWORD + "' | sudo -S chmod 666 /dev/gpiochip0", shell=True)
    run.call("echo '" + PASSWORD + "' | sudo -S chmod 666 /dev/gpiochip1", shell=True)
    run.call("echo '" + PASSWORD + "' | sudo -S chmod 666 /dev/gpiochip2", shell=True)
    
    open_chip()

# Find lines in a chip
try:
    gpio_pin_s = chip1.find_line(HEADER_PIN_7)
    gpio_pin_a = chip1.find_line(HEADER_PIN_18)
except:
    gpio_pin_s = chip2.find_line(HEADER_PIN_7)
    gpio_pin_a = chip2.find_line(HEADER_PIN_18)

# Do configuration
try:
    pin_config_input(gpio_pin_s)
    pin_config_input(gpio_pin_a)
except:
    gpio_pin_s.release()
    gpio_pin_a.release()

    pin_config_input(gpio_pin_s)
    pin_config_input(gpio_pin_a)
    pass

# The shutdown logic
while True:
    time.sleep(0.5)
    try:
        if gpio_pin_a.get_value() == 0:
            if gpio_pin_s.get_value() == 1:
                print("Shutdown!!!")
                run.call("echo '" + PASSWORD + "' | sudo -S shutdown -h now", shell=True)
                #run.call("echo '" + PASSWORD + "' | sudo -S shutdown -r now", shell=True)
            else:
                print("System power ON!")
        else:
            print("Connect Header-Pin 18 to GND for activating Auto-Shutdown.")
    except BaseException as e:
        # Releasing the GPIO pin when it is not used anymore
        gpio_pin_a.release()
        gpio_pin_s.release()
        print(e)
        break
