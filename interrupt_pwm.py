from machine import Pin, PWM
from utime import sleep_ms


def change_duty():
    global duty
    global pwm
    
    duty += 33
    if duty > 100:
        duty = 0
    pwm.duty_u16(int(duty / 100 * ((1 << 16) - 1)))
    print("Duty: {} %".format(duty))


def debounce(f):
    """Software debounce"""
    sleep_ms(3)
    if p2.value():
        f()
    

p2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p2.irq(lambda pin: debounce(change_duty), Pin.IRQ_RISING)

duty = 0
pwm = PWM(Pin(25))
pwm.duty_u16(duty)
print("Duty: {} %".format(duty))
        
         