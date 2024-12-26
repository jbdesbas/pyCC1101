# PyCC1101

A (micro)python lib for operating CC1101 lowcost chipset.
Inspired by : https://github.com/unixb0y/CPY-CC1101

Tested with : 
- ESP32 ✅
- EPS8266 ❔



Datasheet : https://www.ti.com/lit/ds/symlink/cc1101.pdf

## Example

```python
from digitalio import DigitalInOut
import busio, board

from lib import cc1101


myspi = busio.SPI(board.IO18, MOSI=board.IO23, MISO=board.IO19)
cs = DigitalInOut(board.IO5)
gdo0 = DigitalInOut(board.IO22)

tx = cc1101.CC1101(myspi, cs, gdo0)

tx.reset() # Reset chip config

tx.frequency = 868e6 # Set radio frequency to 868MHz

tx.modulation = '2-FSK' # Frequency Shift Keying (binary) modulation

tx.manchester = True # Enable manchester encoding/decoding

tx.send([0xff, 0x3c, 0b10101010]) # send somes bytes
```

## Main methods and properties

- **`baudrate`**: Returns or set the baud rate for radio transmission (in _Bd_ aka symbols per second).
- **`frequency`**: Returns or set the current oscillator or transmission frequency (in _Hz_).
- **`manchester`**: Returns or set Manchester encoding/decoding (_boolean_).
- **`modulation`**: Returns or set the current modulation used for transmission ( `'2-FSK'`, `'GFSK'`, `'ASK/OOK'`, `'4-FSK'`, `'MSK'` ).
- **`packet_length`**
- **`send(data)`**: Emit data. Data must be an array of byte.
- **`reset()`**: Reset chip registers to factory default values.
