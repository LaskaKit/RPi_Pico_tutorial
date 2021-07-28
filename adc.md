## ADC

RPi Pico má 5 ADC (analog to digital converter) kanálů. První 3 kanály (0, 1, 2) jsou vyvedeny na piny. Čtvrtý kanál slouží k měření systémového napětí VSYS a pátý kanál je napojen na vestavěný senzor teploty.

Rozlišení ADC je 12 bitů, to znamená, že můžeme převést analogový signál na číslo od 0 do 4095. V implementaci MicroPythonu je kvůli kompatibilitě s ostatními mikrokontroléry rozlišení transformováno do 16 bitů.

Inicializovat ADC kanál můžeme pomocí čísla kanálu takto:

```python
adc = machine.ADC(0)  # kanal 0 odpovida GP26
adc = machine.ADC(26)  # stejny efekt jako vyse
```

Hodnotu pak dostaneme takto:

```python
hodnota = adc.read_u16()
```

Teď si ukážeme jak získat teplotu ze zabudovaného teplotního senzoru a vypsat do konzole.

```python
import machine
import utime

# 3.3 V = referenční napětí, 65535 = největší číslo, které můžeme uložit do 16 bytů
CONVERSION_FACTOR = 3.3 / 65535

temp_sensor = ADC(4)

while True:
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706 ) / 0.001721
    print("Voltage: " + str(reading) + " V, Temperature: " + str(temperature) + " °C")
    sleep(2)
```

Čísla, která se objevují ve výpočtu nejsou náhodná, vyplývají z vlastností senzoru.
Pří 27 °C je napětí 0,706 V a s každým stupněm navíc se sníží o 1,72 mV.

### Rozcestník
* [Příprava vývojového prostředí](priprava.md)
* [První program](hello.md)
* [ADC](adc.md)
* [PWM](pwm.md)
* [Přerušení](interrupt.md)
