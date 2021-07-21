from machine import Pin, Timer

led = Pin(25, Pin.OUT)
led2 = Pin(0, Pin.OUT)

timer = Timer()
timer2 = Timer()

timer.init(freq = 2, mode = Timer.PERIODIC, callback = lambda timer: led.toggle() )
timer2.init(freq = 8, mode = Timer.PERIODIC, callback = lambda timer: led2.toggle() )
