import os
import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("subfolder", type=str, help="Subfolder name and subfolder to parse")
parser.add_argument("save", type=str, help="Where to save the result")
args = parser.parse_args()

dn = [f.path for f in os.scandir('.') if f.is_dir() and f.name.startswith(args.subfolder + '-')]
flist = []
for dname in dn:
    fn = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dname) for f in filenames if os.path.splitext(f)[1] == '.ttl' and not 'manifest' in f]
    flist.extend(fn)

fn = flist

os.makedirs(args.save, exist_ok=True)

with open(os.path.join(args.save, 'manifest.ttl'), 'w') as fout: 
    fout.write('@prefix atom: <http://lv2plug.in/ns/ext/atom#> .\n')
    fout.write('@prefix lv2: <http://lv2plug.in/ns/lv2core#> .\n')
    fout.write('@prefix pset: <http://lv2plug.in/ns/ext/presets#> .\n')
    fout.write('@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n')
    fout.write('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n')
    fout.write('@prefix state: <http://lv2plug.in/ns/ext/state#> .\n')
    fout.write('@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n')
    
    for dname in dn:
        fout.write('\n')
        with open(os.path.join(dname, 'manifest.ttl'), 'r') as fin:
            data = fin.readlines()

        display = False
        for line in data:
            if ".ttl>" in line:
                display = True
            if display:
                fout.write(line)

for fname in fn:
    shutil.copy(fname, args.save)
