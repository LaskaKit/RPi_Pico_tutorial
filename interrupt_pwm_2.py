from machine import Pin, PWM
from utime import sleep_ms


def increase_duty():
    global duty
    global pwm
    
    if duty < 99:
        duty += 33
        pwm.duty_u16(int(duty / 100 * ((1 << 16) - 1)))
        print("Duty: {} %".format(duty))


def decrease_duty():
    global duty
    global pwm
    
    if duty > 0:
        duty -= 33
        pwm.duty_u16(int(duty / 100 * ((1 << 16) - 1)))
        print("Duty: {} %".format(duty))
    

def debounce(f):
    """Software debounce"""
    state = p2.value()
    sleep_ms(3)
    if p2.value() == state:
        f()
    

p2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
p2.irq(lambda pin: debounce(increase_duty), Pin.IRQ_RISING)

p3 = Pin(0, Pin.IN, Pin.PULL_DOWN)
p3.irq(lambda pin: debounce(decrease_duty), Pin.IRQ_RISING)

duty = 0
pwm = PWM(Pin(25))
pwm.duty_u16(duty)
print("Duty: {} %".format(duty))
        
         