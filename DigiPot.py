""" A simple control class for the Microchip Technology 
MCP413X series digital potentiometer """

# load the spidev library
import spidev
import struct

# initialize spi
spi = spidev.SpiDev()

class DigiPot:

    def __init__(self,bus=0,device=0):
        # open the spi device
        spi.open(bus,device)

    def set_wiper(self,value = 0.5):
        """ Sets the wiper position

            input:
            -----

                value   : a value between 0 and 1 that sets the 
                          relative position of the potentiometer

            output:
            ------

                sends an SPI signal to the digipot to set the relative
                position of the wiper

        """

        # set the bounds of the value
        value = max([0,value])
        value = min([value,1])

        # scale the value
        scaled_value = int(value * 128)

        # set the wiper write bit
        wiper_write = int(0b0000000000000000)

        # send the wiper bit
        spi.xfer([wiper_write,scaled_value])


    def set_rab(self,value = 0.5):
        """ Sets the total resistance

            input:
            -----

                value   : a value between 0 and 1 that sets the 
                          relative position of the potentiometer

            output:
            ------

                sends an SPI signal to the digipot to set the resistor network

        """

        # set the bounds of the value
        value = max([0,value])
        value = min([value,1])

        # scale the value
        scaled_value = int(value * 128)

        # set the wiper write bit
        wiper_write = int(0b0100000000000000)

        # send the wiper bit
        spi.xfer([wiper_write,scaled_value])


if __name__ == "__main__":
    # get the wiper setting from the command line
    import sys
    val = float(sys.argv[1])

    # test the wiper setting function
    mypot = DigiPot()
    mypot.set_wiper(val)




