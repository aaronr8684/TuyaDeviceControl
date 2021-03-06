import sys
import logging
from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD
from tuya_iot import (
    TuyaOpenAPI,
    AuthType,
    TUYA_LOGGER
)

TUYA_LOGGER.setLevel(logging.DEBUG)

DEVICE_IDs = sys.argv[1]
ACTION = sys.argv[2]
VALUE = sys.argv[3]

device_list = DEVICE_IDs.split(',')

# Init
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)

openapi.connect(USERNAME, PASSWORD)

# Do Commands
for DEVICE_ID in device_list:
    if ACTION == 'switch_led':
        commands = {'commands': [{'code': ACTION, 'value': VALUE == 'True'}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

    if ACTION == 'colour_data':
        commands = {'commands': [{'code': 'work_mode', 'value': 'colour'}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        BRIGHT = sys.argv[4]    
        commands = {'commands': [{'code': ACTION, 'value': "{\"h\":"+VALUE+",\"s\":255.0,\"v\":"+BRIGHT+"}"}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        commands = {'commands': [{'code': 'switch_led', 'value': True}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        
    if ACTION == 'bright_value':
        commands = {'commands': [{'code': ACTION, 'value': int(VALUE)}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        commands = {'commands': [{'code': 'switch_led', 'value': True}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
