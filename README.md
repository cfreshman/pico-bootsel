**This has been replaced by an official MicroPython implementation → [rp2.bootsel_button()](https://docs.micropython.org/en/latest/library/rp2.html?highlight=bootsel#rp2.bootsel_button)**
```python
import time, rp2
while True:
  print('BOOTSEL', rp2.bootsel_button())
  time.sleep(1)
```

## pico-bootsel
Credit to [github@pdg137](https://github.com/pdg137)'s comment [here](https://github.com/micropython/micropython/issues/6852#issuecomment-1350081346)  

Read the state of the BOOTSEL button on Raspberry Pi Pico

```python
import time, bootsel
while True:
  print('BOOTSEL', bootsel.pressed())
  time.sleep(1)
```

See [bootsel.py](./bootsel.py) for more info  
See [main.py](./main.py) for example usage  
