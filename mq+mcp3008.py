#!//usr/bin/python3

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board, busio, digitalio, time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

gas_vals = {}
gas_vals[0] = AnalogIn(mcp, MCP.P0)	# MQ-136	Hydrogen Sulfide gas
gas_vals[1] = AnalogIn(mcp, MCP.P1)	# MQ-2		Methane, Butane, LPG, smoke
gas_vals[2] = AnalogIn(mcp, MCP.P2)	# MQ-8		Hydrogen Gas
gas_vals[3] = AnalogIn(mcp, MCP.P3)
gas_vals[4] = AnalogIn(mcp, MCP.P4)
gas_vals[5] = AnalogIn(mcp, MCP.P5)
gas_vals[6] = AnalogIn(mcp, MCP.P6)
gas_vals[7] = AnalogIn(mcp, MCP.P7)

while True:
	# print("Raw ADC Value: ", chan.value)
	ts = time.strftime("%FT%TZ", time.gmtime())
	print(ts, end="")
	for i in range(0,8):
		print("\t", end='')
		print(str(i) + ": {0:0.4f} V".format(gas_vals[i].voltage), end="")

	print("")
	time.sleep(1)
