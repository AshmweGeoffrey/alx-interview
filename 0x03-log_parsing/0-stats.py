#!/usr/bin/python3
""" Log parsing Script
"""


import sys


def printx(data, status):
    """ print the log """
    print("File size: {}".format(data))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0}
counter = 0
data = 0
try:
    for line in sys.stdin:
        if counter == 10:
            printx(data, status)
            counter = 1
        else:
            counter = counter + 1
        parsed = line.split()
        try:
            data = data + int(parsed[-1])
        except Exception as e:
            pass
        try:
            for key, value in status.items():
                if key == parsed[-2]:
                    status[key] = status[key] + 1
        except Exception as e:
            pass
    printx(data, status)
except KeyboardInterrupt as e:
    printx(data, status)
