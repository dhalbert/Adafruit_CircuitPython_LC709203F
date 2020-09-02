# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import time
import board
from adafruit_lc709203f import LC709023F

print("LC709023F simple test")
print("Make sure LiPoly battery is plugged into the board!")

i2c = board.I2C()
sensor = LC709023F(i2c)

print("IC version:", hex(sensor.ic_version))
while True:
    print(
        "Battery: %0.3f Volts / %0.1f %%" % (sensor.cell_voltage, sensor.cell_percent)
    )
    time.sleep(1)
