from machine import Pin
from utime import sleep_ms, localtime

led = Pin(25, Pin.OUT)
led2 = Pin(0, Pin.OUT)


def print_time():
    time = localtime()[3:6]
    print("{}:{}:{}".format(time[0], time[1], time[2]))


def blink(*leds, freq=1):
    for led in leds:
        led.on()
        sleep_ms(1000 // freq // 2)
        led.off()
        sleep_ms(1000 // freq // 2)
        print_time()
    

while True:
    blink(led, led2, freq=4)