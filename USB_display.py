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
def event_json_based_hw_control(event_json, enable_relay_flag, enable_gpio_flag, signal_usb_relay_method, signal_gpio_method):
    try:
        for tmp in event_json['event']['tags']:
            if tmp['key'] == 'lp':
              ser=serial.Serial("/dev/ttyUSB0",9600)
              if not ser.isOpen():
              ser.open()
              print('Serial port is open',ser.isOpen())
              inputString = tmp['value']
              outputString = inputString.encode('utf-8').hex()
              reuslt = r'\x'.join(outputString[i:i+2] for i in range(0, len(outputString), 2))
              def ts(str):
                 command = b"\x30\x30\x32\x44\x49\x53\x3D\x{}\x0D\x0A"
                 ser.write(command)
                 print(command)
    except Exception as err:
        print("Error while triggering relay : ", err)
    return 
