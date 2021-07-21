from machine import ADC
from time import sleep

temp_sensor = ADC(4)

# 3.3 V = referenční napětí, 65535 = největší číslo, které můžeme uložit do 16 bytů
conversion_factor = 3.3 / 65535

while True:
    reading = temp_sensor.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.718 ) / 0.001721
    print("Voltage: " + str(reading) + " V, Temperature: " + str(temperature) + " °C")
    sleep(2)
