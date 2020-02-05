import serial
import time
import json

ser = serial.Serial('COM5', baudrate=19200, timeout=0.1)
time.sleep(3)  # delay required before sending and receiving

values = {
    "pos1": 0,
    "pos2": 35,
    "pos3": 70,
    "pos4": 105,
    "pos5": 140,
    "pos6": 160,
    "counter": 0,
}


def setValues():
    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y


while 1:
    receivedValues = setValues()
    print(receivedValues)
