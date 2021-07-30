## Stmívání LED

RPi Pico má 16 PWM kanálů.

Nejčastějším využitím PWM je regulace výkonu, například LED. Ukážeme si jak pomocí PWM postupně stmívat vestavěnou LED.

```python
from machine import PWM, Pin
from utime import sleep_us

LED_PIN = 25
BLINK_FREQUENCY = 1
PWM_FREQUENCY = 200 # nastavime tak aby lidske oko nedokazalo rozpoznat blikani
                    # hranice je okolo 120 Hz muzete vyzkouset :)

# inicializace
led = Pin(LED_PIN)
pwm = PWM(led, PWM_FREQUENCY)

duty = 0  # duty = strida
direction = 1

while True:
    # overeni jetli se ztmavuje nebo rozsveci
    if duty >= 255:
        direction = -1
    elif duty <= 0:
        direction = 1

    duty += direction
    pwm.duty_u16(duty * duty)

    sleep_us(1_000_000 // BLINK_FREQUENCY // 255 // 2)
```

### Rozcestník
* [Příprava vývojového prostředí](priprava.md)
* [První program](hello.md)
* [ADC](adc.md)
* [PWM](pwm.md)
* [Přerušení](interrupt.md)
* [Morseovka](morse.md)
