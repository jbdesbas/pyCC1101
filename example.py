from machine import SPI, Pin
import cc1101

myspi = SPI(2) # Hardware SPI, MOSI 23, MISO 19, CLK 18

cs = Pin(5, mode=Pin.OUT, value=1)
gdo0 = Pin(22)

tx = cc1101.CC1101(myspi, cs, gdo0)

tx.reset() # Reset chip config

tx.frequency = 868e6 # Set radio frequency to 868Mhz

tx.modulation = '2-FSK' # Frequency Shift Keying (binary) modulation

tx.manchester = True # Enable manchester encoding/decoding
