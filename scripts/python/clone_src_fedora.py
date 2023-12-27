#!/usr/bin/env python3

import requests 
import json
import subprocess

response = requests.get('https://src.fedoraproject.org/extras/pagure_owner_alias.json')
data = json.loads(response.text)
for key in data['rpms'].keys():
    if not 'orphan' in data['rpms'][key]:
        print(key)
        out = subprocess.run(["git", "clone", "https://src.fedoraproject.org/rpms/" + key], capture_output=True)
