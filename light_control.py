import RPi.GPIO as GPIO
import time
import cv2
import mediapipe 

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output(5, False)
GPIO.output(6, False)
GPIO.output(13, False)
GPIO.output(19, False)
GPIO.output(26, False)

for i in range(3):
    GPIO.output(5, True)
    time.sleep(0.1)
    GPIO.output(5, False)
    time.sleep(0.1)
    GPIO.output(6, True)
    time.sleep(0.1)
    GPIO.output(6, False)
    time.sleep(0.1)
    GPIO.output(13, True)
    time.sleep(0.1)
    GPIO.output(13, False)
    time.sleep(0.1)
    GPIO.output(19, True)
    time.sleep(0.1)
    GPIO.output(19, False) 
    time.sleep(0.1)
    GPIO.output(26, True)
    time.sleep(0.1)
    GPIO.output(26, False) 
    
GPIO.output(5, True)
GPIO.output(6, True)
GPIO.output(13, True)
GPIO.output(19, True)
GPIO.output(26, True)
time.sleep(0.5)
GPIO.output(5, False)
GPIO.output(6, False)
GPIO.output(13, False)
GPIO.output(19, False)
GPIO.output(26, False)

def thumb_led(status):
    if status == 1: GPIO.output(26, True)
    elif status == 0: GPIO.output(26, False)
    
def index_led(status):
    if status == 1: GPIO.output(19, True)
    elif status == 0: GPIO.output(19, False)
    
def middle_led(status):
    if status == 1: GPIO.output(13, True)
    elif status == 0: GPIO.output(13, False)
    
def ring_led(status):
    if status == 1: GPIO.output(6, True)
    elif status == 0: GPIO.output(6, False)
    
def pinky_led(status):
    if status == 1: GPIO.output(5, True)
    elif status == 0: GPIO.output(5, False)
    
