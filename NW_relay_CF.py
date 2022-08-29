import json
import sys
import os
import re
from datetime import timedelta
import time
import requests
import threading
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.178', 3300))
print("Before the function################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################")

def event_json_based_hw_control(event_json, enable_relay_flag, enable_gpio_flag, signal_usb_relay_method, signal_gpio_method):
    print("Entered the function")
    print("********************************************************************************************************************************************************************************************************************************************************")
    try:
        for tmp in event_json['event']['tags']:
            if tmp['key'] == 'database':
                if tmp['value'] == 'matched':
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(('192.168.1.178', 3300))
                    my_bytes = bytearray()
                    my_bytes.append(0x01)
                    s.send (my_bytes)
                    s.close()
                    print("Sent 1 to Ardino")
    except Exception as err:
        print("Error while triggering relay : ", err)
    return event_json
