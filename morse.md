### Morzeovka

Zajímavou úlohou na procvičení může být program, který převede text do morseovy abecedy a pomocí LED zobrazí.

Abyste nemuseli dlouze přepisovat morzeovu abecedu do programu, připravili jsme pro vás šablonu.

```python
DELAY = 100                # casova jednotka v ms [cj], urcuje rychlost
DELAY_DOT = 1 * DELAY      # tecka trva 1 cj
DELAY_DASH = 3 * DELAY     # carka trva 2 cj
DELAY_SYMBOLS = 1 * DELAY  # prodleva mezi jednotlivymi symboly je 1 cj
DELAY_LETTERS = 3 * DELAY  # prodleva mezi pismeny jsou 3 cj
DELAY_WORDS = 7 * DELAY    # prodleva mezi slovy je 7 cj

table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
    }
```
