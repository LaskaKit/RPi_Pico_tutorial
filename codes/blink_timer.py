from machine import Pin, Timer

led = Pin(25, Pin.OUT)

tim = Timer(freq=1, mode=Timer.PERIODIC, callback=lambda _: led.toggle())

