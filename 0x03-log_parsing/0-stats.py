#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics: """

import sys

def status_check(line):
    splited_line=line.split(' ')
    try:
        if (splited_line[4] == "\"GET" and 
            len(splited_line)==9 and 
            splited_line[5] == "/projects/260" and 
            splited_line[6] == "HTTP/1.1\""):
            result={"code":splited_line[7],"file_size":splited_line[8]}
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
            status[obtained_result["code"]] += 1
            file_size += int(obtained_result["file_size"])
            count += 1
        if count == 9:
            print_metrics()
            count=0
except KeyboardInterrupt:
    print_metrics()
