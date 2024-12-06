import requests
import json
from static import secrets


#For security purposes, secrets will not be imported into GitHub. Please provide your own credentials.

ubuser = secrets.ub_user
ubtoken = secrets.ub_token

# requesting data
url = 'https://vault.evocative.com/api/2.0/?method=device.list&dev_desc='
server = str(input("Input data here:"))
url2 = "&require_ip=1"
ubersmith_call = requests.get(url+server+url2, auth=(ubuser, ubtoken))

#parsing data

ubersmith_data = json.loads(ubersmith_call.content)

device_id = list(ubersmith_data['data'].keys())[0]

for assignment in ubersmith_data['data'][device_id]['assignments'].values():
    if assignment ['assign_description'] == 'IPMI':
        ipmi_address = assignment['addr_readable']
        break

#prepping the package 

split = ipmi_address.split('.')
subnet = "255.255.255.0"
gateway1 = str(split[0]+"."+split[1]+"."+split[2])
gateway2 = ".1"
gateway = gateway1 + gateway2

