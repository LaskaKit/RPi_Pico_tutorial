Interrupt (přerušení): procesor dokončí rozpracovanou inkstrukci, vykoná akce související s přerušením a poté pokračuje tam kde skončil.

Díky přerušení není potřeba odchytávat události ve while loopu. Jednoduchost kódu ++ :D

Ukážeme si na příkladu blikající LED. Pomocí přerušení budeme měnít frekvenci, se kterou bliká.

```python
from machine import Pin
from utime import sleep_us

led = Pin(25, Pin.OUT)
freq = 1

def freq_to_delay(freq):
    """Hz to delay in ms"""
    return 1000000 // freq // 2


def change_freq():
    global freq
    freq *= 2
    if freq > 1 << 7:
        freq = 1
    print("{} Hz".format(freq))


def debounce(f):
    """Software debounce"""
    sleep_us(300)
    if p2.value():
        f()


p2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p2.irq(lambda pin: debounce(change_freq), Pin.IRQ_RISING)


print("{} Hz".format(freq))
while True:
    led.toggle()
    sleep_us(freq_to_delay(freq))
```

<div class="footer" style="display: flex; justify-content: space-around">
    <a href="hello.md">Příprava vývojového prostředí</a>
</div>
