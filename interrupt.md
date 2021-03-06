# KOD NETESTOVAN

## Přerušení (interrupt)

Když procesor dostane signál o přerušení, tak nejprve dokončí rozpracovanou inkstrukci, poté vykoná akce související s přerušením a poté pokračuje tam kde předtím skončil.

Díky přerušení není potřeba odchytávat události ve while loopu.

Ukážeme si na příkladu blikající LED. Pomocí přerušení budeme měnít frekvenci, se kterou bliká.

```python
from machine import Pin, disable_irq, enable_irq
from utime import sleep_us

led = Pin(25, Pin.OUT)
freq = 1

def freq_to_delay(freq):
    """Hz to delay in us"""
    return 1000000 // freq // 2


def change_freq():
    global freq
    freq *= 2
    if freq > 1 << 7:
        freq = 1
    print("{} Hz".format(freq))


def debounce(fn):
    disable_irq()
    fn()
    sleep_us(300)
    enable_irq()


p2 = Pin(0, Pin.IN, Pin.PULL_DOWN)  # neni potreba zapojovat externi PULL UP nebo PULL DOWN rezistor, Pico je ma v sobe integrovane, staci jen nastavit v kodu
p2.irq(lambda _: debounce(change_freq), Pin.IRQ_RISING)  # preruseni nastane pri nabezne hrane a vykona se funkce change_freq
# funkci jsme obalili softwarovym debouncem, coz neni idealni, ale funguje


print("{} Hz".format(freq))
while True:
    led.toggle()
    sleep_us(freq_to_delay(freq))
```

### Rozcestník
* [Příprava vývojového prostředí](priprava.md)
* [První program](hello.md)
* [ADC](adc.md)
* [PWM](pwm.md)
* [Přerušení](interrupt.md)
* [Morseovka](morse.md)
