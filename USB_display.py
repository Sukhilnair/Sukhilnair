import codecs
import json
import sys
import os
import re
import serial
from datetime import timedelta
import time
import requests
import threading
import socket
print ("##########################################################inside client format####################################################")
def event_json_based_hw_control(event_json, enable_relay_flag, enable_gpio_flag, signal_usb_relay_method, signal_gpio_method):
    try:
        value = event_json['event']['name']
        ser=serial.Serial("/dev/ttyUSB0",9600)
        ser.close()
        ser.open()
        print('Serial port is open',ser.isOpen())
        inputString = "002DIS="+value[0:8]
        print(inputString)
        outputString = inputString.encode('utf-8').hex()
        print(outputString)
        reuslt = r"\x"+r'\x'.join(outputString[i:i+2] for i in range(0, len(outputString), 2))
        print (reuslt)
        command = "b"+'"'+reuslt+'"'
        sent = reuslt.encode()
        print (sent)
        rece = (reuslt.encode()).decode('unicode-escape')
        rece += "\r\n"
        print (rece.encode())
        ser.write(rece.encode())
    except Exception as err:
        print("Error while triggering relay : ", err)
    return
