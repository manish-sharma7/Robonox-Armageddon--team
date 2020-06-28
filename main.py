from Barcode import barcode
from snapshot import snapshot
from angle import angle
import robot-control
from time import sleep
import RPi.GPIO as GPIO

imgPath = "tmp.png"
degrees={}

def act():
    """

    Arguments: None
    Returns: degrees to be twisted by the bot

    """
    snapshot()
    pin_code = str(barcode(imgPath))
    degrees,amount = angle(degrees,pin_code)
    return pin_code

def drop():
    """
        argument: none
        returns: void
    """
    #functionality to drop the item

def pickup():
    """
        argument: none
        returns: void
    """
    #functionality to pick the item

#------some physical variables depending on the hardware---
#Closes Blocker
time_gap = 3
#Opens blocker
GPIO.setmode(GPIO.BOARD)
pwm=GPIO.PWM(03, 50)
pwm.start(0)
#----------------------------------------------------------

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

while(True):
    pickup()
    deg = act()
    SetAngle(deg)
    drop()
    SetAngle(360-deg)
    sleep(1)
