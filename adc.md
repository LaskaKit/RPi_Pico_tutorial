## Čtení z vestavěného teploměru

Teplota se bude vypisovat do konzole.

```python
from machine import ADC
from time import sleep

# 3.3 V = referenční napětí, 65535 = největší číslo, které můžeme uložit do 16 bytů
CONVERSION_FACTOR = 3.3 / 65535

temp_sensor = ADC(4)

while True:
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.718 ) / 0.001721
    print("Voltage: " + str(reading) + " V, Temperature: " + str(temperature) + " °C")
    sleep(2)
```

### Rozcestník
* [Příprava vývojového prostředí](priprava.md)
* [První program](hello.md)
* [ADC](adc.md)
* [PWM](pwm.md)
* [Přerušení](interrupt.md)
