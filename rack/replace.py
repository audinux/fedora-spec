#!/usr/bin/python3

import fileinput
import sys
import json
import shutil
import subprocess
import glob
import os

path_to_library_git = 'library'
path_to_spec_files = 'spec'

# this script must be started a level before the 'library' rack repo
# A directory 'spec' with a file 'template.spec' containing the tag SLUGNAME, VERSION, COMMITID and SOURCEURL must be created

def get_git_revision_hash(git_path):
    curr_path = os.getcwd()
    os.chdir(git_path)
    commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode("utf-8")
    os.chdir(curr_path)
    return commit_id.rstrip()

def proceed(json_file):
    # read json file
    # skip some files:
    if 'Core.json' in json_file:
        return
    if 'VCV-Prototype.json' in json_file:
        return
    if 'settings.json' in json_file:
        return
    
    print('Reading %s json library file\n' % json_file)
    
    with open(json_file, 'r') as fjson:
        conf_rack = json.load(fjson)
        if 'license' in conf_rack and conf_rack['license'] == 'proprietary':
            print('Proprietary license\n')
            return
        if 'license' in conf_rack and conf_rack['license'] == 'Proprietary':
            print('Proprietary license\n')
            return
        if 'license' in conf_rack and conf_rack['license'] == 'PROPRIETARY':
            print('Proprietary license\n')
            return
        
        slug_name   = conf_rack['slug']
        version     = conf_rack['version']
        if 'sourceUrl' in conf_rack:
            sourceurl = conf_rack['sourceUrl'].replace('.git','') # remove the trailing '.git'
        else:
            sourceurl = ''
        description = ''
        if 'modules' in conf_rack and 'description' in conf_rack['modules'][0]:
            description = conf_rack['modules'][0]['description']

        if not os.path.exists(path_to_spec_files + os.sep + 'template.spec'):
            print('template file not found in %s\n' % path_to_spec_files + os.sep)
            sys.exit(-1)
        
        if not os.path.exists(path_to_library_git + os.sep + 'repos' + os.sep + slug_name):
            print('repos slug_name doesn\'t exists\n')
            return
        
        commit_id = get_git_revision_hash(path_to_library_git + os.sep + 'repos' + os.sep + slug_name)

        print('SLUGNAME    -> %s\n' % slug_name)
        print('VERSION     -> %s\n' % version)
        print('SOURCEURL   -> %s\n' % sourceurl)
        print('COMMITID    -> %s\n' % commit_id)
        print('DESCRIPTION -> %s\n' % description)
        
        spec_filename = 'rack-v1-library-' + slug_name + '.spec'
        
        # copy template into spec file
        shutil.copyfile(path_to_spec_files + os.sep + 'template.spec', path_to_spec_files + os.sep + spec_filename)
        # copy json file into spec dire
        shutil.copyfile(json_file, path_to_spec_files + os.sep + slug_name + '_plugin.json')
        
        #with fileinput.FileInput(path_to_spec_files + os.sep + spec_filename, inplace=True, backup='.bak') as file:
        with fileinput.FileInput(path_to_spec_files + os.sep + spec_filename, inplace=True) as file:
            for line in file:
                if 'SLUGNAME' in line:
                    print(line.replace('SLUGNAME',  slug_name), end='')
                elif 'VERSION' in line:
                    print(line.replace('VERSION',   version), end='')
                elif 'COMMITID' in line:
                    print(line.replace('COMMITID',  commit_id), end='')
                elif 'SOURCEURL' in line:
                    print(line.replace('SOURCEURL', sourceurl), end='')
                elif 'DESCRIPTION' in line:
                    if description:
                        print(line.replace('DESCRIPTION', description), end='')
                elif 'JSONFILE' in line:
                    print(line.replace('JSONFILE', slug_name + '_plugin.json'), end='')
                else:
                    print(line, end='')
    
if __name__ == "__main__":
    if len(sys.argv) != 1:
        proceed(path_to_library_git + os.sep + 'manifests' + os.sep + sys.argv[1] + '.json')
    else:
        # we iterate through library/manifests/*.json and we generate spec/*.spec
        for json_file in glob.glob(path_to_library_git + os.sep + 'manifests' + os.sep + '*.json'):
            proceed(json_file)
