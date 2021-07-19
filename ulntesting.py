from machine import Pin
from utime import sleep_ms

pins = [Pin(i, Pin.OUT) for i in range(4)]


states = [[1, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 1],
          [1, 0, 0, 1]]

states_simple = [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]]


def set_pins(state):
    for i in range(len(pins)):
        pins[i].value(state[i])

while True:
    for i in range(len(states)):
        set_pins(states[-i])
        sleep_ms(2)
        

    