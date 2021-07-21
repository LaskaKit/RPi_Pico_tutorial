
# Začínáme s Raspberry Pi Pico

## Obsah

* [Instalace MicroPython](#instalace-micropython)
* [Programování](#programování)
* [Hello, Pico!](#hello)
* [Rozložení pinů](#rozložení-pinů)
+ [RPI_Pico_example_codes](#rpi-pico-example-codes)

## Instalace MicroPython

1.	Stáhněte si [U2F soubor](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2) s MicroPythonem.
2.	Se stisknutým tlačítkem BOOTSEL připojte Pico k počítači pomocí USB kabelu.
3.	Pico se zobrazí jako vyměnitelné úložište se jménem RPI-RP2.
4.	Přetáhněte U2F soubor do RPI-RP2. Pico se samo restartuje a spustí se MicroPython interpreter.

## Programování

Rpi Pico se dá naprogramovat v C/C++, MicroPythonu nebo v assembleru. My si ukážeme tu nejjednodušší možnost a to je jednoznačně MicroPython.

Základní workflow: napsat skript, uložit ho s příponou `.py` do úložiště Pica a skript se spustí. Skript se bude spouštět automaticky se zapnutím Pica. Pro nahrání jiného skriptu je zase třeba připojit Pico s držením BOOTSEL tlačítka.

Existují však IDE, které práci zjednodušují tak, že není potřeba pro každou změnu ve skriptu Pico vypínat a zapínat. Doporučeným IDE pro programování RPi Pico v jazyce Python je [Thonny IDE](https://thonny.org/). Dále budeme používat právě Thonny.


Po instalaci spusťte Thonny a v nástrojové liště postupujte tímto způsobem:

1.	Běh -> Vybrat interpreter…
2.	V dialogovém okně vyberte MicroPython (Raspberry Pi Pico) a automatickou detekci portu můžete ponechat.

Pokud vše proběhlo správně, tak by dole v konzoli měl běžet interpreter MicroPython na RPi Pico.

Odteď můžeme s Pico interagovat buď přímo přes konzoli, anebo psát skripty a uploadovat je.


## Hello, Pico! {#hello}

```
>>> print("Hello, Pico!")
Hello, Pico!
>>>>
```

Dalším krokem bude rozblikání vestavěné LED. Místo konzole už použijeme samotný editor.

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

Po přepsání stačí kliknout na zelené tlačítko v horní liště a skript se spustí. Když ho budeme chtít zastavit, stačí kliknout na červené tlačítko zastavit.

## Rozložení pinů

![RPi pico pin layout](images/pico_layout.png)

### RPI_Pico_example_codes
dalsi materialy

[Datasheet](https://datasheets.raspberrypi.org/pico/pico-datasheet.pdf)

[Python SDK](https://datasheets.raspberrypi.org/pico/raspberry-pi-pico-python-sdk.pdf)

[MicroPython](https://micropython.org/)
