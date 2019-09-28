import serial

from subprocess import Popen, PIPE

ser=serial.Serial(port="/dev/ttyUSB1")



def keypress(sequence):
    p = Popen(['xte'], stdin=PIPE)
    p.communicate(input=sequence)



while True:
    key,value=ser.readline().decode("ascii").strip().split(": ")
    value = int(value)
    if key == "Switch" and value == 0:
        print(value)
        keypress(b"key a\n")
    
    if key == "X-axis" and value >= 800:
        print(value)
        keypress(b"key Up\n")
    
    if key == "X-axis" and value <= 255:
        print(value)
        keypress(b"key Down\n")
        
    if key == "Y-axis" and value >= 800:
        print(value)
        keypress(b"key Right\n") 
        
    if key == "Y-axis" and value <= 255:
        print(value)
        keypress(b"key Left\n") 
        
