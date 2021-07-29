from machine import Pin
from utime import sleep_ms


DELAY = 100  # ms
DOT = 1
DASH = 3
SPACE_BETWEEN_SYMBOLS = 1
SPACE_BETWEEN_LETTERS = 3
SPACE_BETWEEN_WORDS = 7

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
            blink(DELAY * DOT)
        elif item == '-':
            blink(DELAY * DASH)
        sleep_ms(DELAY * SPACE_BETWEEN_SYMBOLS)
            

def blink_morse(string):
    for letter in string.lower():
        if letter == ' ':
            sleep_ms(DELAY * SPACE_BETWEEN_WORDS - DELAY * SPACE_BETWEEN_LETTERS)
        else:
            blink_letter(letter)
            sleep_ms(DELAY * SPACE_BETWEEN_LETTERS - DELAY * SPACE_BETWEEN_SYMBOLS)
       
       
def make_morse_string(string):
    morse_string = ''
    for letter in string.lower():
        if letter == ' ':
            morse_string += '/ '
        else:
            morse_string += table[letter] + ' '   
    return morse_string
    

led = Pin(25, Pin.OUT)

sentence = 'sos'

while True:    
    print(sentence)
    print(make_morse_string(sentence))
    blink_morse(sentence)
    print()