# TuyaDeviceControl
A quick and dirty method for sending commands from the CLI via the [official Tuya Python SDK](https://github.com/tuya/tuya-iot-python-sdk)

This is used by me for sending commands from a Stream Deck to Tuya compatible devices

## Setup
### Requires env.py file with the following values
- ACCESS_ID
- ACCESS_KEY
- USERNAME
- PASSWORD
- ENDPOINT - [see list here](https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4#title-1-Endpoints)

### CLI Args (all required for now)
1. Device_ID (22 char hex, also called 'id' in API)
2. Command/action to send
3. Value for action (bool or int based on command type)
4. Brightness value (25-255) for color command (only required for 'colour_data' command)


### Example requests
- Turn light off

`python.exe lights.py abcd1234ef567890abcd12 switch_led False`

- Change color to red (H of HSV to zero) and set brightness (V of HSV) to 50%

`python.exe lights.py abcd1234ef567890abcd12 colour_data 0 115`



## Prerequisites

### Registration

Please check [Tuya IoT Platform Configuration Guide](https://developer.tuya.com/en/docs/iot/Platform_Configuration_smarthome?id=Kamcgamwoevrx) to register an account on the [Tuya IoT Platform](https://iot.tuya.com?_source=github), and get the required information. You need to create a Cloud project and complete the configuration of asset, user, and application. Then, you will get the **username**, **password**, **Access ID**, and **Access Secret**.

## Installation of Tuya SDK

`pip3 install tuya-iot-py-sdk`
