import serial
import keyboard
from subprocess import Popen, PIPE

ser = serial.Serial(port="/dev/ttyUSB1")


def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)


while True:
    key, value = ser.readline().decode("ascii").strip().split(": ")
    value = int(value)
    if key == "Switch" and value == 0:
        print(value)
        keyboard.press("a")
    
    if key == "X-axis" and value >= 800:
        print(value)
        keyboard.press("up")
    
    if key == "X-axis" and value <= 255:
        print(value)
        keyboard.press("down")
        
    if key == "Y-axis" and value >= 800:
        print(value)
        keyboard.press("right")
        
    if key == "Y-axis" and value <= 255:
        print(value)
        keyboard.press("left")
        
