#!/usr/bin/env python

import webbrowser
import time
#import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
while(True):
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()

    if (id==939506745260):
        print("Hello")
        webbrowser.open('https://thefitbox.netlify.app/workout')  # Go to example.com
    elif (id==589776086361):
        webbrowser.open('https://thefitbox.netlify.app/workout1')  # Go to example.com
    #os.system("xdg-open \"\" https://example.com")

