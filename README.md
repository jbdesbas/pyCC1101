# PyCC1101

A (micro)python lib for operating CC1101.
Inspired by : https://github.com/unixb0y/CPY-CC1101

This library can be used to easily work with the low+cost (less than 2€) and fully-featured CC1101 tranceiver.
Provide fine control over transmission such as modulation (FSK, ASK, etc.), frequency, deviation, baud rate and more.
Additionally, it offers chip-level data control inluding manchester encoding/decoding, checksum and address filtering.

> [!IMPORTANT]
> This library is currently under active development. No release yet.

Tested with : 

Boards :
- ESP32 ✅
- EPS8266 ❔

Environment:
- CircuitPython ✅
- MicroPython ❔

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
tx.baudrate = 38400
tx.preset_tx() # Apply basiC TX preset

# Send only payload
tx.append_status = False
tx.white_data = False
tx.sync_mode = 0
tx.crc = False


tx.send([0xff, 0x3c, 0b10101010]*10) # send somes bytes
```

## Main methods and properties

- **`append_status`**:
- **`baudrate`**: Returns or set the baud rate for radio transmission (in _Bd_ aka symbols per second).
- **`deviation`**: Returns or set deviation (in Hz). Affect FSK modulation.
- **`crc`**:
- **`frequency`**: Returns or set the current oscillator or transmission frequency (in _Hz_).
- **`length_config`**: Returns or set packet length config ( `'fixed'`, `'variable'`, `'infinite'` ).
- **`manchester`**: Returns or set Manchester encoding/decoding (_boolean_).
- **`modulation`**: Returns or set the current modulation used for transmission ( `'2-FSK'`, `'GFSK'`, `'ASK/OOK'`, `'4-FSK'`, `'MSK'` ).
- **`pa_table`**: Returns or set PA_TABLE (8-bytes array)/
- **`packet_length`**: Returns or set packet length (see `length_config`)
- **`send(data)`**: Emit data. Data must be an array of byte.
- **`sync_mode`**:
- **`white_data`**:
- **`reset()`**: Reset chip registers to factory default values.

All chip parameters can be accessed using `write_config` or `read_config` (ex : `write_config(PKTCTRL0, WHITE_DATA, 0x1)` ).
See [datasheet](https://www.ti.com/lit/ds/symlink/cc1101.pdf) for all parameters.
