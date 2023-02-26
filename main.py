"""
pico-bootsel: read the state of the BOOTSEL button

Credit to github@pdg137 (see bootsel.py)
Drop bootsel.py into your MicroPython projects

Here's an example which toggles the on-board LED:
"""

import bootsel, time, machine


led = machine.Pin('LED', machine.Pin.OUT)
led.value(1)
while True:
  if bootsel.pressed():
    led.value(0 if led.value() else 1)
    print('BOOTSEL pressed, LED', 'on' if led.value() else 'off')
    while bootsel.pressed():
      time.sleep(.1)
  time.sleep(.1)
