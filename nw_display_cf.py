import codecs
import json
import sys
import os
import re
from datetime import timedelta
import time
import requests
import threading
import socket
def event_json_based_hw_control(event_json, enable_relay_flag, enable_gpio_flag, signal_usb_relay_method, signal_gpio_method):
    try:
        for tmp in event_json['event']['tags']:
            if tmp['key'] == 'lp':
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host ="192.168.1.96"
                port =65432
                s.connect((host,port))
                inputString = tmp['value']
                outputString = inputString.encode('utf-8').hex()
                def ts(str):
                   send = ("30 30 31 44 49 53 3D {} 0D 0A".format(outputString))
                   s.send(send.encode())
                   print (send)
                   data = ''
                   data = s.recv(1024).decode()
                   print (data)
    except Exception as err:
        print("Error while triggering relay : ", err)
    return event_json
