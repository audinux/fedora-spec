#!/usr/bin/env python3

import requests  
import json
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform thirdparty analysis')
    parser.add_argument('--match', dest='match', type=str, default=None, help='Check for package matching string. Nothing for all')
    parser.add_argument('--stat', dest='stat', default=False, action='store_true', help='Compute some stats on orphaned / other')
    args = parser.parse_args()

    response = requests.get('https://src.fedoraproject.org/extras/pagure_owner_alias.json')
    data = json.loads(response.text)

    #print(data.keys())
    #for key in data.keys():
    #    print(f"{key}:")
    #    for key2 in data[key].keys():
    #        print(f"  - {key2}")
    
    if args.stat:
        not_orphaned = 0
        orphaned = 0
        for key in data['rpms'].keys():
            if 'orphan' in data['rpms'][key]:
                orphaned += 1
            else:
                not_orphaned += 1

        print(f"Orphaned packages: {orphaned}")
        print(f"Active packages: {not_orphaned}")
        print(f"Total packages: {orphaned + not_orphaned}")
    else:
        for key in data['rpms'].keys():
            if args.match:
                if args.match in key and 'orphan' in data['rpms'][key]:
                    print(key)
            else:
                if 'orphan' in data['rpms'][key]:
                    print(key)
       
