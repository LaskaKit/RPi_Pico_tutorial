from machine import Pin
from utime import sleep_ms


DELAY = 100                # casova jednotka v ms, urcuje rychlost
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


def blink(time):
    global led
    led.on()
    sleep_ms(time)
    led.off()


def blink_letter(letter):
    for item in table[letter]:
        if item == '.':
            blink(DELAY_DOT)
        elif item == '-':
            blink(DELAY_DASH)
        sleep_ms(DELAY_SYMBOLS)


def blink_morse(string):
    for letter in string.lower():
        if letter == ' ':
            sleep_ms(DELAY_WORDS - DELAY_LETTERS)
        else:
            blink_letter(letter)
            sleep_ms(DELAY_LETTERS - DELAY_SYMBOLS)


def make_morse_string(string):
    morse_string = ''
    for letter in string.lower():
        if letter == ' ':
            morse_string += '/ '
        else:
            morse_string += table[letter] + ' '
    return morse_string


led = Pin(25, Pin.OUT)

sentence = 'by Makers for Makers'

while True:
    print(sentence)
    print(make_morse_string(sentence))
    print()

    sleep_ms(DELAY_WORDS - DELAY_LETTERS)
    blink_morse(sentence)
