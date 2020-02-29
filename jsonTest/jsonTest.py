import serial
import time
import json

ser = serial.Serial('/dev/ttyUSB3', baudrate=19200, timeout=0.1)
time.sleep(3)  # delay required before sending and receiving
position = 0

values = {
    "pos1": 0,
    "pos2": 0,
    "pos3": 0,
    "pos4": 0,
    "pos5": 0,
    "pos6": 0,
    "counter": 0,
}


def setValues(pos1,pos2,pos3):
    values["pos1"] = pos3
    values["pos2"] = 180 - pos1
    values["pos3"] = pos1
    values["pos4"] = 180 - pos2
    values["pos5"] = pos2
    values["pos6"] = 180 - pos3


    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y


while 1:
    print("================================================")
    print("Current positions: pos1=", values["pos1"]," pos2=", values["pos2"]," pos3=", values["pos3"]," pos4=", values["pos4"]," pos5=", values["pos5"]," pos6=", values["pos6"])
    print("Input format: pos1 pos2 pos3")
    pos1, pos2, pos3 = input("Enter your values: ").split()
    receivedValues = setValues(int(pos1),int(pos2),int(pos3))
    print(receivedValues)
