#!/usr/bin/python3

import requests

# put your keys in the header
headers = {
    "app_id": "5f42a8ee",
    "app_key": "196b5a215bff2a34feaeb976b6a9266f"
}

payload = '{"image":"http://34.243.236.218/image/sanjay.jpg","gallery_name":"sanjaysface", "subject_id":"Sanjay"}'

url = "http://api.kairos.com/enroll"

# make request
r = requests.post(url, data=payload, headers=headers)
print (r.content.decode('utf-8'))