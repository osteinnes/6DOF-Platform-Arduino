import serial
import time
import json

ser = serial.Serial('/dev/ttyUSB2', baudrate=19200, timeout=0.1)
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
    values["pos1"] = pos1
    values["pos2"] = 180 - pos1
    values["pos3"] = pos2
    values["pos4"] = 180 - pos2
    values["pos5"] = pos3
    values["pos6"] = 180 - pos3


    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y

def setSixPositions(p1,p2,p3,p4,p5,p6):
    values["pos1"] = p6
    values["pos2"] = 180 - p1
    values["pos3"] = p2
    values["pos4"] = 180 - p3
    values["pos5"] = p4
    values["pos6"] = 180 - p5


    ser.write(str.encode(json.dumps(values)))  # convert to json format, convert to bytes, write to serial port
    data = ser.readline()  # read input, convert to ascii string
    y = json.loads(data)  # convert string to python object
    values["counter"] += 1  # increment counter for testing
    return y

def runTranslationExample():
    simulation = True
    positions = [150, 150, 150]
    y = setValues(positions[0],positions[1],positions[2])

    low=80
    high=140
    
    first = True
    while first:
        positions[0]-=2
        if positions[0]<low:
            first=False
            break
        y = setValues(positions[0],positions[1],positions[2])
        print(y)
    second=True
    while second:
        positions[1]-=2
        if positions[1]<low:
            positions[0]+=2
            if positions[0]>high:
                second=False
                break
        y = setValues(positions[0],positions[1],positions[2])
        print(y)
    third=True
    while third:
        positions[2]-=2
        if positions[2]<low:
            positions[1]+=2
            if positions[1] > high:
                third=False
                break
        y = setValues(positions[0],positions[1],positions[2])
        print(y)
    fourth = True
    while fourth:
        positions[2]+=2
        if positions[2]>high:
            fourth=False
            break
        y = setValues(positions[0],positions[1],positions[2])
        print(y)
        #for i in range(3):
        #    positions[i] -= 10
        #    y = setValues(positions[0],positions[1],positions[2])
        #    time.sleep(0.5)


        
def runTranslationExampleTwo(times):
    for i in range(times):
        high = 130
        low = 80
        y = setValues(high,high,high)
        y = setValues(low,high,high)
        y = setValues(low,low,high)
        y = setValues(high,low,high)
        y = setValues(high,low,low)
        y = setValues(high,high,low)
        y = setValues(high,high,high)


#runTranslationExampleTwo(3)
while 1:
    print("================================================")
    print("Current positions: pos1=", values["pos1"]," pos2=", values["pos2"]," pos3=", values["pos3"]," pos4=", values["pos4"]," pos5=", values["pos5"]," pos6=", values["pos6"])
    print("Input format: pos1 pos2 pos3")
    pos1, pos2, pos3 = input("Enter your values: ").split()
    receivedValues = setValues(int(pos1),int(pos2),int(pos3))
    print(receivedValues)
    
