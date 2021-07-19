from machine import Pin, Timer
from utime import sleep_ms

led = Pin(25, Pin.OUT)
freq = 1


def freq_to_delay(freq):
    """Hz to delay in ms"""
    return 1000000 // freq // 2


def change_freq():
    global freq
    global timer
    freq *= 2
    if freq > 1 << 7:
        freq = 1

    #timer.deinit()
    timer.init(freq=freq * 2, mode=Timer.PERIODIC, callback=lambda timer: led.toggle())
    print("{} Hz".format(freq))


def switch(f):
    """Software debounce"""
    sleep_ms(3)
    if p2.value():
        f()


p2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p2.irq(lambda pin: switch(change_freq), Pin.IRQ_RISING)

timer = Timer()

print("{} Hz".format(freq))
timer.init(freq=freq * 2, mode=Timer.PERIODIC, callback=lambda timer: led.toggle())
