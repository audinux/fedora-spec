import os
import glob
import sys
import subprocess
import json


def get_files(path, extension):
    """
    A generator of filepaths for each file into path with the target extension.
    If recursive, it will loop over subfolders as well.
    """
    for root, dirs, files in os.walk(path):
        for file_path in glob.iglob(root + "/*." + extension):
            yield file_path


if __name__ == '__main__':
    spec_dict = {}
    spec_files = sorted(get_files('..', 'spec'))
    tags = set()
    spec_type_list = [
        'clap',
        'dssi',
        'ladspa',
        'lv2',
        'plugin',
        'standalone',
        'vamp',
        'vst',
        'vst2',
        'vst3',
    ]

    for _file in spec_files:
        print(f"Processing {_file} ...")
        with open(_file, 'r') as fin:
            name = None
            tag = []
            for line in fin.readlines():
                if 'Name:' in line:
                    name = line.replace('Name:', '').strip().lower()
                if '# Type:' in line:
                    tag = line.replace('# Type:', '').strip().split(',')
                    tag = [_tag.strip().lower() for _tag in tag if _tag]
                    if not any([_tag for _tag in tag if _tag in spec_type_list]):
                        break
                    tags.update(tag)
                if tag and name:
                    if name not in spec_dict:
                        spec_dict[name] = {
                            'file': _file,
                            'tag': tag,
                            'dnf_type': [],
                            'found': True,
                        }
                    else:
                        print(f"Error: {name} already found in dict: {_file}")
                        
                    break

    type_list = [
        'vamp',
        'vst',
        'vst2',
        'vst3',
        'ladspa',
        'lv2',
        'dssi',
        'clap',
        'standalone',
    ]
    
    for _type in type_list:
        print(f"Processing {_type} ...")
        cmd = ['dnf', 'search', '--repoid=copr:copr.fedorainfracloud.org:ycollet:audinux', _type + '-']
        out = subprocess.run(cmd, capture_output=True)
        for line in out.stdout.decode().split('\n'):
            if "debug" in line or 'src' in line or 'i686' in line:
                continue
            if 'x86_64' in line:
                name = line.split('.x86_64')[0].strip()
                if not name.startswith('rack-'):
                    if name not in spec_dict:
                        # some spec names start with 'ladspa-' or other types ...
                        name = name.replace(_type + '-', '', 1).strip().lower()
                else:
                    name = name.strip().lower()
                    
                if name not in spec_dict:
                    print(f"Error: {name} not found")
                    spec_dict[name] = {
                        'file': None,
                        'tag': [],
                        'dnf_type': [_type],
                        'found': False,
                    }
                    
                    continue

                print(f"Adding {_type.lower()} to {name}")
                spec_dict[name]['dnf_type'].append(_type.lower())

    print("#\n#\n#")
    print("# Checking")
    print("#\n#\n#")

    for name, val in spec_dict.items():
        if not all([True if _tag in val['dnf_type'] else False for _tag in val['tag']]):
            print(f"{name}: miss some types: {','.join(val['tag'])} / {','.join(val['dnf_type'])}")
            
    for name, val in spec_dict.items():
        if not val['found']:
            print(f"{name}: was not found")
