#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics: """

import sys

def status_check(line):
    splited_line=line.split()
    try:
        result={"code":splited_line[-2],"file_size":splited_line[-1]}
        return result
    except IndexError:
        pass
    return None
def print_metrics():
    print("File size: {}".format(file_size))
    for key,data in status.items():
        if data !=0:
            print("{}: {}".format(key,data))
    count=0
status = {"200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0}
file_size=0
count=0
try:
    for line in sys.stdin:
        obtained_result=status_check(line)
        if obtained_result != None:
            try:
                status[obtained_result["code"]] += 1
            except Exception as e:
                pass
            try:
                file_size += int(obtained_result["file_size"])
            except Exception as e:
                pass
            count += 1
        if count == 10:
            print_metrics()
            count=1
except KeyboardInterrupt as e:
    print_metrics()
