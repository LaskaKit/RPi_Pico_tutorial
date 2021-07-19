from machine import ADC, PWM, Pin
from utime import sleep_ms

LED_PIN = 25
PWM_FREQUENCY = 200

pwm = PWM(Pin(LED_PIN))
pwm.freq(PWM_FREQUENCY)

adc_in = ADC(0)

# 3.3 V = referenční napětí, 65535 = největší číslo, které můžeme uložit do 16 bytů
conversion_factor = 3.3 / 65535

while True:
    reading = adc_in.read_u16()
    voltage = reading * conversion_factor

    # uvazeni odchylky
    if reading <= 500:
        reading = 0
    elif reading >= 65360:
        reading = 65535

    print("Voltage: " + str(voltage) + " reading " + str(reading))
    pwm.duty_u16(reading)
    sleep_ms(30)
