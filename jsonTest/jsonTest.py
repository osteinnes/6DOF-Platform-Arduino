import serial
import time
import json

ser = serial.Serial('COM6', baudrate=19200, timeout=0.1)
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


def setValues(position):
    values["pos1"] = position
    values["pos2"] = 180 - position
    values["pos3"] = position
    values["pos4"] = 180 - position
    values["pos5"] = position
    values["pos6"] = 180 - position


    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y


while 1:
    val = input("Enter your value: ")
    receivedValues = setValues(int(val))
    print(receivedValues)
