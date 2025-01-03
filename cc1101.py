from adafruit_bus_device.spi_device import SPIDevice
from time import sleep

WRITE_SINGLE_BYTE = 0x00
WRITE_BURST = 0x40
READ_SINGLE_BYTE = 0x80
READ_BURST = 0xC0

IOCFG2 = 0x00  # GDO2 Output Pin Configuration
IOCFG1 = 0x01  # GDO1 Output Pin Configuration
IOCFG0 = 0x02  # self.GDO0 Output Pin Configuration
FIFOTHR = 0x03  # RX FIFO and TX FIFO Thresholds
SYNC1 = 0x04  # Sync Word, High Byte
SYNC0 = 0x05  # Sync Word, Low Byte
PKTLEN = 0x06  # Packet Length
PKTCTRL1 = 0x07  # Packet Automation Control
PKTCTRL0 = 0x08  # Packet Automation Control
ADDR = 0x09  # Device Address
CHANNR = 0x0A  # Channel Number
FSCTRL1 = 0x0B  # Frequency Synthesizer Control
FSCTRL0 = 0x0C  # Frequency Synthesizer Control
FREQ2 = 0x0D  # Frequency Control Word, High Byte
FREQ1 = 0x0E  # Frequency Control Word, Middle Byte
FREQ0 = 0x0F  # Frequency Control Word, Low Byte
MDMCFG4 = 0x10  # Modem Configuration
MDMCFG3 = 0x11  # Modem Configuration
MDMCFG2 = 0x12  # Modem Configuration
MDMCFG1 = 0x13  # Modem Configuration
MDMCFG0 = 0x14  # Modem Configuration
DEVIATN = 0x15  # Modem Deviation Setting
MCSM2 = 0x16  # Main Radio Control State Machine Configuration
MCSM1 = 0x17  # Main Radio Control State Machine Configuration
MCSM0 = 0x18  # Main Radio Control State Machine Configuration
FOCCFG = 0x19  # Frequency Offset Compensation Configuration
BSCFG = 0x1A  # Bit Synchronization Configuration
AGCCTRL2 = 0x1B  # AGC Control
AGCCTRL1 = 0x1C  # AGC Control
AGCCTRL0 = 0x1D  # AGC Control
WOREVT1 = 0x1E  # High Byte Event0 Timeout
WOREVT0 = 0x1F  # Low Byte Event0 Timeout
WORCTRL = 0x20  # Wake On Radio Control
FREND1 = 0x21  # Front End RX Configuration
FREND0 = 0x22  # Front End TX Configuration
FSCAL3 = 0x23  # Frequency Synthesizer Calibration
FSCAL2 = 0x24  # Frequency Synthesizer Calibration
FSCAL1 = 0x25  # Frequency Synthesizer Calibration
FSCAL0 = 0x26  # Frequency Synthesizer Calibration
RCCTRL1 = 0x27  # RC Oscillator Configuration
RCCTRL0 = 0x28  # RC Oscillator Configuration

# Configuration Register Details - Registers that Loose Programming in SLEEP State

FSTEST = 0x29  # Frequency Synthesizer Calibration Control
PTEST = 0x2A  # Production Test
AGCTEST = 0x2B  # AGC Test
TEST2 = 0x2C  # Various Test Settings
TEST1 = 0x2D  # Various Test Settings
TEST0 = 0x2E  # Various Test Settings

# Command Strobe Registers

SRES = 0x30  # Reset chip
SFSTXON = 0x31  # Enable and calibrate frequency synthesizer (if MCSM0.FS_AUTOCAL=1).
# If in RX (with CCA): Go to a wait state where only the synthesizer
# is running (for quick RX / TX turnaround).

SXOFF = 0x32  # Turn off crystal oscillator.
SCAL = 0x33  # Calibrate frequency synthesizer and turn it off.
# SCAL can be strobed from IDLE mode without setting manual calibration mode.

SRX = 0x34  # Enable RX. Perform calibration first if coming from IDLE and MCSM0.FS_AUTOCAL=1.
STX = 0x35  # In IDLE state: Enable TX. Perform calibration first
# if MCSM0.FS_AUTOCAL=1.
# If in RX state and CCA is enabled: Only go to TX if channel is clear.

SIDLE = 0x36  # Exit RX / TX, turn off frequency synthesizer and exit Wake-On-Radio mode if applicable.
SWOR = 0x38  # Start automatic RX polling sequence (Wake-on-Radio)
# as described in Section 19.5 if WORCTRL.RC_PD=0.

SPWD = 0x39  # Enter power down mode when CSn goes high.
SFRX = 0x3A  # Flush the RX FIFO buffer. Only issue SFRX in IDLE or RXFIFO_OVERFLOW states.
SFTX = 0x3B  # Flush the TX FIFO buffer. Only issue SFTX in IDLE or TXFIFO_UNDERFLOW states.
SWORRST = 0x3C  # Reset real time clock to Event1 value.
SNOP = 0x3D  # No operation. May be used to get access to the chip status byte.

PATABLE = 0x3E  # PATABLE
TXFIFO = 0x3F  # TXFIFO
RXFIFO = 0x3F  # RXFIFO

# Status Register Details

PARTNUM = 0xF0  # Chip ID
VERSION = 0xF1  # Chip ID
FREQEST = 0xF2  # Frequency Offset Estimate from Demodulator
LQI = 0xF3  # Demodulator Estimate for Link Quality
RSSI = 0xF4  # Received Signal Strength Indication
MARCSTATE = 0xF5  # Main Radio Control State Machine State
WORTIME1 = 0xF6  # High Byte of WOR Time
WORTIME0 = 0xF7  # Low Byte of WOR Time
PKTSTATUS = 0xF8  # Current GDOx Status and Packet Status
VCO_VC_DAC = 0xF9  # Current Setting from PLL Calibration Module
TXBYTES = 0xFA  # Underflow and Number of Bytes
RXBYTES = 0xFB  # Overflow and Number of Bytes
RCCTRL1_STATUS = 0xFC  # Last RC Oscillator Calibration Result
RCCTRL0_STATUS = 0xFD  # Last RC Oscillator Calibration Result

PA_TABLE = [0x00, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Detail  - Config (register, startbit, endbit)
GDO2_INV = (IOCFG2, 6, 6)
GDO2_CFG = (IOCFG2, 0, 5)

GDO_DS = (IOCFG1, 7, 7)
GDO1_INV = (IOCFG1, 6, 6)
GDO1_CFG = (IOCFG1, 5, 0)

TEMP_SENSOR_ENABLE = (IOCFG0, 7, 7)
GDO0_INV = (IOCFG0, 6, 6)
GDO0_CFG = (IOCFG0, 0, 5)

# [...] TODO
PACKET_LENGTH = (PKTLEN, 0, 7)

PQT = (PKTCTRL1, 5, 7)
CRC_AUTOFLUSH = (PKTCTRL1, 3, 3)
APPEND_STATUS = (PKTCTRL1, 2, 2)
ADR_CHK = (PKTCTRL1, 0, 1)

WHITE_DATA = (PKTCTRL0, 6, 6)
PKT_FORMAT = (PKTCTRL0, 4, 5)
CRC_EN = (PKTCTRL0, 2, 2)
LENGTH_CONFIG = (PKTCTRL0, 0, 1)

# [...] TODO

FREQ_IF = (FSCTRL1, 0, 4)

FREQOFF = (FSCTRL0, 0, 7)

# [...] TODO? Freq

CHANBW_E = (MDMCFG4, 6, 7)
CHANBW_M = (MDMCFG4, 4, 5)
DRATE_E = (MDMCFG4, 0, 3)

DRATE_M = (MDMCFG3, 0, 7)

DEM_DCFILT_OFF = (MDMCFG2, 7, 7)
MOD_FORMAT = (MDMCFG2, 4, 6) # Modulation 2FSK, GFSK, etc..
MANCHESTER_EN = (MDMCFG2, 3, 3)
SYNC_MODE = (MDMCFG2, 0, 2)

FEC_EN = (MDMCFG1, 7, 7)
NUM_PREAMBLE = (MDMCFG1, 4, 6)
CHANSPC_E = (MDMCFG1, 0, 1)

CHANSPC_M = (MDMCFG0, 0, 7)

DEVIATION_E = (DEVIATN, 4, 6)
DEVIATION_M = (DEVIATN, 0, 2)


# [...]

# Modulations type
FSK2 = 0x0
GFSK = 0x1
ASK_OOK = 0x3
FSK4 = 0x4
MSK = 0x7



def baudrate_calculation(f_xosc, drate_e, drate_m):
    """ See https://www.ti.com/lit/ds/symlink/cc1101.pdf p.76"""
    return  ( ((256 + drate_m) * 2**drate_e) /(2**28) ) * f_xosc

def deviation_calculation(f_xosc, deviation_e, deviation_m):
    return (f_xosc / 2**17) * (8+ deviation_m) * (2**deviation_e)

class CC1101:
    modulation_label = {'2-FSK': FSK2, 'GFSK': GFSK, 'ASK/OOK': ASK_OOK, '4-FSK': FSK4, 'MSK': MSK}
    packet_config_label = {'fixed': 0x0, 'variable': 0x1, 'infinite':0x2}
    maybe_should_reset = "Maybe you should reset chip by using reset() ?"

    def __init__(self, spi, cs, gdo0):
        self.gdo0 = gdo0
        self.f_xosc = 26e6 # 26 MHz
        self.device = SPIDevice(spi, cs, baudrate=50000, polarity=0, phase=0)
    
    def read_register(self, register):
        """Read whole register"""
        return self.readSingleByte(register)
    
    def read_config(self, register, field):
        """Read register and extract field"""
        if field[0] != register:
            raise Exception (f'Bad field in register {self.register}. The field must be set for {field[0]} register')
        reg_ct = self.read_register(register)
        mask = (1 << (1+field[2] - field[1]) ) - 1
        return (reg_ct >> field[1]) & mask
    
    def write_config(self, register, field, value):
        """
        Write a configuration field into a register.
        Ensures the field matches the register and verifies that the value is within the allowed range.
        Example: write_config(IOCFG2, GDO2_INV, 0x00)
        """
        # Check mapping field/register
        if field[0] != register:
            raise Exception (f'Bad field in register {self.register_address}. The field must be set for {field[0]} register')
        
        # Check value n_bit
        if not value <= (1 << (1+field[2]-field[1]) ):
            raise ValueError (f'Value ovesized ! Must be <= {(1 << (1+field[2]-field[1]) )} ({(1+field[2]-field[1])} bits)') # Factoriser (1 << (1+field[2]-field[1]) )
        
        current_value = self.read_register(register) # Read whole register
        suppr_mask = (1 << (1+field[2]-field[1]))  -1   << field[1] # masque pour supprimer les bits concernés par la mise à jour
        suppr_mask = ~suppr_mask & 0xFF # inversion des bits et limite à 8bits
        new_value = (current_value & suppr_mask) | (value << field[1])
        self.writeSingleByte(register, new_value )
        #return new_value # Applique le masque de suppression et ajoute la nouvelle valeur du paramètre
        
    
    def readSingleByte(self, address):
        databuffer = bytearray([READ_SINGLE_BYTE | address, 0x00])
        
        with self.device as d:
            d.write(databuffer, end=1)
            d.readinto(databuffer, end=2)
        return databuffer[0]
    
    def readBurst(self, start_address, length):        
        databuffer = []
        ret = bytearray(length+1)
        
        for x in range(length + 1):
            addr = (start_address + (x*8)) | READ_BURST
            databuffer.append(addr)
        
        with self.device as d:
            d.write_readinto(bytearray(databuffer), ret)
        return ret
    
    def writeBurst(self, address, data):
        temp = list(data)
        temp.insert(0, (WRITE_BURST | address))
        with self.device as d:
            d.write(bytearray(temp))
    
    def writeSingleByte(self, address, byte_data):
        databuffer = bytearray([WRITE_SINGLE_BYTE | address, byte_data])
        with self.device as d:
            d.write(databuffer)

    def strobe(self, address):
        databuffer = bytearray([address, 0x00])
        with self.device as d:
            d.write(databuffer, end=1)
            d.readinto(databuffer, end=2)
        return databuffer

    def reset(self):
        """Reset chip config (SRES)"""
        self.strobe(SRES)

    def send(self, data, blocking=True):
        """Emit data.
        Data must be a bytearray (eg : bytearray([0b11001100, 245, 0xfc]) or an int array (<256)
        """
        self.strobe(SIDLE)
        while (self.readSingleByte(MARCSTATE) & 0x1F != 0x01): # wait for CC to enter idle state
            pass

        self.strobe(SFTX) # flush TX FIFO
        sleep(0.05)

        self.writeBurst(TXFIFO, data)
        self.strobe(STX)
        sleep(2)         # TODO : wait until all transmited if blocking (read buffer)
        self.strobe(SFTX)
        self.strobe(SFRX)
        sleep(0.05)



    @property
    def manchester(self):
        """ Get or set manchester encoding/decoding
        """
        return self.read_config(MDMCFG2, MANCHESTER_EN) == 0b1

    @manchester.setter
    def manchester(self, value: bool):
        self.write_config(MDMCFG2, MANCHESTER_EN, 0b1 if value else 0b0)

    @property
    def baudrate(self):
        drate_e = self.read_config(MDMCFG4, DRATE_E)
        drate_m = self.read_config(MDMCFG3, DRATE_M)
        return baudrate_calculation(self.f_xosc, drate_e, drate_m)

    @baudrate.setter
    def baudrate(self, value: int):
        """Get or set baudrate (baud, Bd).
        The actual baud rate returned might be slightly different from the requested baud rate
        due to the constraints of the CC1101's register values and the limited precision
        of the calculation.
        """
        # TODO handle OOB error
        for e in range(1, 16): # Exponent (4 bits)
            if baudrate_calculation(self.f_xosc, e, 0) > value :
                drate_e = e-1
                break

        for m in range(1, 256): # Mantis (8 bits)
            if baudrate_calculation(self.f_xosc, drate_e, m) > value :
                drate_m = m-1
                break

        self.write_config(MDMCFG4, DRATE_E, drate_e)
        self.write_config(MDMCFG3, DRATE_M, drate_m)
    
    @property
    def deviation(self):
        """Get or set deviation (Hz).
        The actual deviation returned might be slightly different from the requested baud rate
        due to the constraints of the CC1101's register values and the limited precision
        of the calculation.
        """
        deviation_e = self.read_config(DEVIATN, DEVIATION_E)
        deviation_m = self.read_config(DEVIATN, DEVIATION_M)
        return deviation_calculation(self.f_xosc, deviation_e, deviation_m)
        
    @deviation.setter
    def deviation(self, value):
        # TODO : nested loops and take closest ?
        for e in range(1, 8): # Exponent (3 bits)
            if deviation_calculation(self.f_xosc, e, 0) > value :
                deviation_e = e-1
                break
        
        for m in range(1, 8): # Mantis (3 bits)
            if deviation_calculation(self.f_xosc, deviation_e, m) > value :
                deviation_m = m-1
                break
        
        self.write_config(DEVIATN, DEVIATION_E, deviation_e)
        self.write_config(DEVIATN, DEVIATION_M, deviation_m)
    
    @property
    def length_config(self):
        register_value = self.read_config(PKTCTRL0, LENGTH_CONFIG)
        try:
            return next(key for key, value in self.packet_config_label.items() if value == register_value)
        except StopIteration:
            raise Exception(f"{hex(register_value)} : unknown length config. {self.maybe_should_reset}")
            
    @length_config.setter
    def length_config(self, value):
        try:
            self.write_config(PKTCTRL0, LENGTH_CONFIG, self.packet_config_label[value])
        except KeyError:
            raise Exception(f"Invalid length config, must be one of : {' | '.join(self.packet_config_label.keys())}")
    
    @property
    def frequency(self):
        """ Get or set radio frequency
        The step is about 400Hz with a 26 MHz crystal ( fxosc / 2**16 ).
        """
        x = (self.readSingleByte(FREQ2) << 16) | (self.readSingleByte(FREQ1) << 8) | (self.readSingleByte(FREQ0))
        return (self.f_xosc / 2**16) * x
        
    @frequency.setter
    def frequency(self, value):
        x = round(value / (self.f_xosc / 2**16))
        self.writeSingleByte(FREQ2, (x >> 16) & 0xff)
        self.writeSingleByte(FREQ1, (x >> 8) & 0xff)
        self.writeSingleByte(FREQ0, x & 0xff)
    
    @property
    def modulation(self):
        register_value = self.read_config(MDMCFG2, MOD_FORMAT)
        try:
            return next(key for key, value in self.modulation_label.items() if value == register_value)
        except StopIteration:
            raise Exception(f"{hex(register_value)} : unknown modulation type. {self.maybe_should_reset}")

    @modulation.setter
    def modulation(self, value):
        try:
            self.write_config(MDMCFG2, MOD_FORMAT, self.modulation_label[value])
        except KeyError:
            raise Exception(f"Invalid modulation format, must be one of : {' | '.join(self.modulation_map.keys())}")

    @property
    def packet_length(self):
        """Get or set packet length (PKTLEN)
        """
        return self.read_config(PKTLEN, PACKET_LENGTH)
    
    @packet_length.setter
    def packet_length(self, value):
        self.write_config(PKTLEN, PACKET_LENGTH, value)
        
    def preset_tx(self):
        """Apply some config preset for optimized tx"""
        self.writeBurst(PATABLE, PA_TABLE)      
        self.writeSingleByte(IOCFG2, 0x29)    #0
        self.writeSingleByte(IOCFG1, 0x2E)    #0
        self.writeSingleByte(IOCFG0, 0x06)   #0

        self.writeSingleByte(FSCTRL1, 0x08)  #0 
        self.writeSingleByte(FSCTRL0, 0x00)   #0    
             
        self.write_config(MDMCFG4,CHANBW_E,0b11)
        self.write_config(MDMCFG4,CHANBW_M,0b11) # Attention baudrate

        #self.writeSingleByte(MDMCFG3, 0x10)   #0 
        #self.writeSingleByte(MDMCFG2, 0x32)   #0
        #self.writeSingleByte(MDMCFG1, 0x22)   #0
        #self.writeSingleByte(MDMCFG0, 0xF8) #0

        #self.writeSingleByte(DEVIATN, 0x00)   #0
        self.writeSingleByte(MCSM2, 0x07) #0
        self.writeSingleByte(MCSM1, 0x30) #0    
        self.writeSingleByte(MCSM0, 0x18) #0
        self.writeSingleByte(FOCCFG, 0x16) #0 ?
        self.writeSingleByte(BSCFG, 0x6C) #1 ? # Nécessaire

        self.writeSingleByte(FIFOTHR, 0x47)   #0

        self.writeSingleByte(AGCCTRL2,0x06) # 0 # AGGCTRL Nécessiare
        self.writeSingleByte(AGCCTRL1,0x00) # 0
        self.writeSingleByte(AGCCTRL0, 0x95) # 0

        self.writeSingleByte(WORCTRL, 0xFB) #0

        self.writeSingleByte(FREND0, 0x11)  #0

        self.writeSingleByte(FSCAL3, 0xE9) #0
        self.writeSingleByte(FSCAL2, 0x2A) #0
        self.writeSingleByte(FSCAL1, 0x00) #0
        self.writeSingleByte(FSCAL0, 0x1F) #0

        # Bilan : Ces réglages sembles nécessaire.
        # A voir si possibilité d'améliorer le gain
    
    def setupTX(self): # dev
        self.writeSingleByte(IOCFG2, 0x29)    
        self.writeSingleByte(IOCFG1, 0x2E)    
        self.writeSingleByte(IOCFG0, 0x06)    
        self.writeSingleByte(FIFOTHR, 0x47)   
        self.writeSingleByte(PKTCTRL1, 0x00)  
        self.writeSingleByte(PKTCTRL0, 0x00)  
        self.writeSingleByte(ADDR, 0x00)
        self.writeSingleByte(CHANNR, 0x00)
        self.writeSingleByte(FSCTRL1, 0x06)   
        self.writeSingleByte(FSCTRL0, 0x00)   
        self.writeSingleByte(MDMCFG4, 0xE7)    
        self.writeSingleByte(MDMCFG3, 0x10)    
        self.writeSingleByte(MDMCFG2, 0x30)    #. 32 would be 16/16 sync word bits .#
        self.writeSingleByte(MDMCFG1, 0x22)   
        self.writeSingleByte(MDMCFG0, 0xF8)
        self.writeSingleByte(DEVIATN, 0x15)   
        self.writeSingleByte(MCSM2, 0x07)
        self.writeSingleByte(MCSM1, 0x20)     
        self.writeSingleByte(MCSM0, 0x18)
        self.writeSingleByte(FOCCFG, 0x14)
        self.writeSingleByte(BSCFG, 0x6C)
        self.writeSingleByte(AGCCTRL2, 0x03)  
        self.writeSingleByte(AGCCTRL1, 0x00)  
        self.writeSingleByte(AGCCTRL0, 0x92)
        self.writeSingleByte(WOREVT1, 0x87)
        self.writeSingleByte(WOREVT0, 0x6B)
        self.writeSingleByte(WORCTRL, 0xFB)
        self.writeSingleByte(FREND1, 0x56)    
        self.writeSingleByte(FREND0, 0x11)    
        self.writeSingleByte(FSCAL3, 0xE9)
        self.writeSingleByte(FSCAL2, 0x2A)
        self.writeSingleByte(FSCAL1, 0x00)
        self.writeSingleByte(FSCAL0, 0x1F)
        self.writeSingleByte(RCCTRL1, 0x41)
        self.writeSingleByte(RCCTRL0, 0x00)
        self.writeSingleByte(FSTEST, 0x59)
        self.writeSingleByte(PTEST, 0x7F)   
        self.writeSingleByte(AGCTEST, 0x3F)
        self.writeSingleByte(TEST2, 0x81)     
        self.writeSingleByte(TEST1, 0x35)     
        self.writeSingleByte(TEST0, 0x0B)
    
