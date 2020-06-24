import serial
import keyboard

ser = serial.Serial(port=" ") #You can find the port in the arduino IDE

while True:
    key, value = ser.readline().decode("ascii").strip().split(": ")
    value = int(value)
    if key == "Switch" and value == 0:
        print(value)
        keyboard.press("a")
        keyboard.press("page up")
    
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
        
