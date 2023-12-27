#!/usr/bin/env python3

import requests 
import json

response = requests.get('https://src.fedoraproject.org/extras/pagure_owner_alias.json')
data = json.loads(response.text)
for key in data['rpms'].keys():
    #if 'dssi' in key and 'orphan' in data['rpms'][key]:
    #    print(key)
    if not 'orphan' in data['rpms'][key]:
        print(key)
