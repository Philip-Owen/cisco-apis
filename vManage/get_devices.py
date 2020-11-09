import requests
import sys

# Root URL to access vManage "https://vManage-ip:port"
base_url = "https://sandbox-sdwan-1.cisco.com/"

# Security Check endpoint to create session with vManage server
security_check = "j_security_check"

# User credentials to authenticate to the vManage dashboard
user = {
    'j_username': "devnetuser",
    'j_password': "RG!_Yw919_83d"
}

# Establish session with vManage Server
session = requests.session()
auth = session.post(f"{base_url}{security_check}", data=user, verify=False)

# Exit if authenticaiton fails
if not auth.ok or auth.text:
    print("Authenticaiton failed")
    sys.exit(1)

# Send request to devices endpoint to GET a list of all devices in vManage 
# and print the Hostname, Device ID, System IP, Site ID, and Model for
# each device.
devices = "dataservice/device"
device_list = session.get(f"{base_url}{devices}", verify=False).json()
for d in device_list['data']:
    print('\n**************\n')
    print(f"{d['host-name']}")
    print(f"    Device ID: {d['deviceId']}")
    print(f"    System IP: {d['system-ip']}")
    print(f"    Site ID: {d['site-id']}")
    print(f"    Model: {d['device-model']}")

