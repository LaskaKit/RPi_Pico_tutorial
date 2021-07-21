from machine import Pin
from utime import sleep_ms


def throw():
    global number
    print(number + 1)


def debounce(f):
    """Software debounce"""
    sleep_ms(3)
    if p2.value():
        f()
    

p2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p2.irq(lambda pin: debounce(throw), Pin.IRQ_RISING)


number = 0
while True:
    number = (number + 1) % 6
    
        
         