import machine
from utime import sleep_ms

# PIR connected to D7
pir = machine.Pin(13, machine.Pin.IN)
led = machine.Pin(2, machine.Pin.OUT, value=1)

while True:
    # check if PIR sensor detected motion = needs a repeatable setting
    if pir.value():
        led.value(0)
        # this delay should conform to the PIR sensor one
        sleep_ms(5000)
        if not pir.value():
            led.value(1)
