## Rozblikání vestavěné LED

Jedním z prvních kroků při seznamování se s novým hardware je rozblikání LED. K RPi Pico nemusíme žádnou zapojovat, má jednu zabudovanou.

```python
# modul machine slouzi k ovladani hardware
# pro rozblikani LED budeme potrebovat tridu Pin
from machine import Pin
from utime import sleep

# vestavena LED je napojena na pin 25, nejprve je potreba pin inicializovat
led = Pin(25, Pin.OUT)

# ted uz staci jen prepinat mezi HIGH a LOW, nejjednoduseji pomoci metody toggle()
while True:
    led.toggle()
    sleep(1)
```

LED můžeme rozblikat i pomocí třídy `Timer`, která využívá hardwarový časovač:

```python
from machine import Pin, Timer

led = Pin(25, Pin.OUT)

tim.init(freq=1, mode=Timer.PERIODIC, callback=lambda _: led.toggle())
```


## Hello, Pico!

Dalším krokem bývá vypsání "Hello, World!" přes USB serial nebo UART. Pokud používate Thonny IDE a jste připojeni RPi Pico tak stačí do konzole napsat:

```python
print("Hello, Pico!")
```

### Rozcestník
* [Příprava vývojového prostředí](priprava.md)
* [První program](hello.md)
* [ADC](adc.md)
* [PWM](pwm.md)
* [Přerušení](interrupt.md)
