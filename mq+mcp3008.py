#!//usr/bin/python3

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board, busio, digitalio, time, sys
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

sys.path.append('/home/ghz/wxlib')
import wxlib as wx

wx_dir = "/home/ghz/repos/mq_gases"
dat_fname = "gas_levels"


spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

gas_vals = {}
gas_vals_sum = {}

for i in range(0,8):
	gas_vals_sum[i] = 0
itr = 0

gas_vals[0] = AnalogIn(mcp, MCP.P0)	# MQ-136	Hydrogen Sulfide gas
gas_vals[1] = AnalogIn(mcp, MCP.P1)	# MQ-2		Methane, Butane, LPG, smoke
gas_vals[2] = AnalogIn(mcp, MCP.P2)	# MQ-8		Hydrogen Gas
gas_vals[3] = AnalogIn(mcp, MCP.P3)	# MQ-135	Air Quality (Benzene, Alcohol, smoke)
gas_vals[4] = AnalogIn(mcp, MCP.P4)	# MQ-7		Carbon Monoxide
gas_vals[5] = AnalogIn(mcp, MCP.P5)
gas_vals[6] = AnalogIn(mcp, MCP.P6)
gas_vals[7] = AnalogIn(mcp, MCP.P7)

while True:
	# print("Raw ADC Value: ", chan.value)
	ts = time.strftime("%FT%TZ", time.gmtime())
	print(ts, end="")
	for i in range(0,8):
		gas_vals_sum[i] += gas_vals[i].voltage
		print("\t", end='')
		print(str(i) + ": {0:0.4f} V".format(gas_vals[i].voltage), end="")
	print("")
	itr += 1

	if itr >= 57:
		dat_s = "{0:s}".format(ts)
		for i in range(0,8):
			dat_s += "\t"
			dat_s += str(i) + ": {0:0.4f} V".format(gas_vals_sum[i] / itr)

		dat_s += "\n"

		itr = 0
		for i in range(0,8):
			gas_vals_sum[i] = 0

		wx.write_out_dat_stamp_iso(ts, dat_fname, dat_s, wx_dir)
	time.sleep(1)
