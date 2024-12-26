from digitalio import DigitalInOut
import busio, board

from lib import cc1101


myspi = busio.SPI(board.IO18, MOSI=board.IO23, MISO=board.IO19)
cs = DigitalInOut(board.IO5)
gdo0 = DigitalInOut(board.IO22)

tx = cc1101.CC1101(myspi, cs, gdo0)
tx.reset() # Reset chip config

tx.frequency = 868e6 # Set radio frequency to 868Mhz
