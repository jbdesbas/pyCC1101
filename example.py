from digitalio import DigitalInOut
import busio, board

from lib import cc1101


myspi = busio.SPI(board.IO18, MOSI=board.IO23, MISO=board.IO19)
cs = DigitalInOut(board.IO5)
gdo0 = DigitalInOut(board.IO22)

tx = cc1101.CC1101(myspi, cs, gdo0)

tx.read_register(cc1101.MDMCFG2)

tx.write_config(cc1101.MDMCFG2, cc1101.DEM_DCFILT_OFF, 0b01)


tx.read_register(cc1101.MDMCFG2)
