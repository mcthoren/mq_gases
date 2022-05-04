#!/usr/bin/python3

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# thanks to Adafruit for all the docs, boards and code.
# docs and example code from here:
# https://learn.adafruit.com/mcp3008-spi-adc?view=all

# datasheet here:
# https://cdn-shop.adafruit.com/datasheets/MCP3008.pdf

import board, busio, digitalio, time, sys
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

sys.path.append('/home/ghz/wxlib')
import wxlib as wx

wx_dir = "/home/ghz/repos/mq_gases"
dat_fname = "gas_levels"

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs0 = digitalio.DigitalInOut(board.D5)
cs1 = digitalio.DigitalInOut(board.D6)
mcp0 = MCP.MCP3008(spi, cs0)
mcp1 = MCP.MCP3008(spi, cs1)

gas_vals = {}
gas_vals_sum = {}

itr = 0
num_sens = 16

for i in range(num_sens):
	gas_vals_sum[i] = 0

gas_vals[0] = AnalogIn(mcp0, MCP.P0)	# MQ-136	Hydrogen Sulfide
gas_vals[1] = AnalogIn(mcp0, MCP.P1)	# MQ-2		Methane, Butane, LPG, Smoke
gas_vals[2] = AnalogIn(mcp0, MCP.P2)	# MQ-8		Hydrogen
gas_vals[3] = AnalogIn(mcp0, MCP.P3)	# MQ-135	Air Quality (Benzene, Alcohol, Smoke)
gas_vals[4] = AnalogIn(mcp0, MCP.P4)	# MQ-7		Carbon Monoxide
gas_vals[5] = AnalogIn(mcp0, MCP.P5)	# MQ-3		Alcohol, Ethanol, Smoke
gas_vals[6] = AnalogIn(mcp0, MCP.P6)	# MQ-5		Natural Gas, LPG
gas_vals[7] = AnalogIn(mcp0, MCP.P7)	# MQ-4		Methane, CNG
gas_vals[8] = AnalogIn(mcp1, MCP.P0)	# MQ-6		LPG, Butane
gas_vals[9] = AnalogIn(mcp1, MCP.P1)	# MQ-9		"Methane, Propane, etc. Combustible Gas" (only running at 5VDC)
gas_vals[10] = AnalogIn(mcp1, MCP.P1)	# MQ-137	Ammonia
gas_vals[11] = AnalogIn(mcp1, MCP.P1)
gas_vals[12] = AnalogIn(mcp1, MCP.P1)
gas_vals[13] = AnalogIn(mcp1, MCP.P1)
gas_vals[14] = AnalogIn(mcp1, MCP.P1)
gas_vals[15] = AnalogIn(mcp1, MCP.P1)

while True:
	# print("Raw ADC Value: ", chan.value)
	ts = time.strftime("%FT%TZ", time.gmtime())
	print(ts, end="")
	for i in range(num_sens):
		gas_vals_sum[i] += gas_vals[i].voltage
		print("\t", end='')
		print(str(i) + ": {0:0.4f} V".format(gas_vals[i].voltage), end="")
	print("")
	itr += 1

	if itr >= 57:
		dat_s = "{0:s}".format(ts)
		for i in range(num_sens):
			dat_s += "\t"
			dat_s += str(i) + ": {0:0.4f} V".format(gas_vals_sum[i] / itr)

		dat_s += "\tpi_temp: {0:0.2f} °C\n".format(float(wx.pi_temp_read()) / 1000)

		itr = 0
		for i in range(num_sens):
			gas_vals_sum[i] = 0

		wx.write_out_dat_stamp_iso(ts, dat_fname, dat_s, wx_dir)
	time.sleep(1)
