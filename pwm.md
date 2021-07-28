## Stmívání LED

RPi Pico má 16 PWM kanálů

Nšjčastějším využitím PWM je regulace výkonu, například stmívání LED. Ukážeme si jak pomocí PWM stmívat vestavěnou LED.

![PWM](images/pwm.png)
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FPWM-signal-with-its-two-basic-time-periods_fig4_271437313&psig=AOvVaw10SVsBpZIkFZGVLsW6Senh&ust=1626953737873000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLDa_JiJ9PECFQAAAAAdAAAAABAE

```python
from machine import PWM, Pin
from utime import sleep_us

LED_PIN = 25
BLINK_FREQUENCY = 1
PWM_FREQUENCY = 200 # nastavime tak aby lidske oko nedokazalo rozpoznat blikani
                    # hranice je okolo 120 Hz muzete vyzkouset

# inicializace
led = Pin(LED_PIN)
pwm = PWM(led, PWM_FREQUENCY)

duty = 0
direction = 1

while True:
    # overeni jetli se ztmavuje nebo rozsveci
    if duty >= 255:
        direction = -1
    elif duty <= 0:
        direction = 1

    # nastaveni nove hodnoty "duty"
    duty += direction
    pwm.duty_u16(duty * duty)

    # nechceme aby se smycka vykonavala nekontrolovane rychle,
    # to by zpusobilo jen ztmaveni
    sleep_us(1_000_000 // BLINK_FREQUENCY // 255 // 2)
```

<div class="footer" style="display: flex; justify-content: space-around">
    <a href="README.md">Obsah</a>
</div>
