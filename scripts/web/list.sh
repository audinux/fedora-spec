# ---------------------------------------------------------------------------------
#!/bin/bash
set -e


REPO_ID=$(dnf -q repolist | grep ycollet | cut -d\  -f1)

# Character improbable
Q=$(echo -e '\u2621')

QF="{${Q}name${Q}:${Q}%{name}${Q},${Q}version${Q}:${Q}%{version}${Q},${Q}url${Q}:${Q}%{url}${Q},${Q}license${Q}:${Q}%{license}${Q},${Q}summary${Q}:${Q}%{summary}${Q},${Q}category${Q}:${Q}${Q},${Q}tags${Q}:[],${Q}type${Q}:[],${Q}description${Q}:${Q}%{description}${Q}},"

dnf repoquery --repoid=$REPO_ID --latest-limit 1 --arch=src --qf $QF > list.js

# Replace ALL newlines with an improbable character
tr '\n' '\a' < list.js > list2.js

# 1/ At the end of a line put back a new line, after "}," (slight risk to have it in a description)
# 2/ In other cases, put a \n
# 3/ Escape all "
# 4/ Replace the special character $Q by a a real quote
# 5/ Remove the last ,

sed -i "s/},\a/},\n/g ; s/\a/\\\\n/g ; s/\"/\\\\\"/g ; s/$Q/\"/g ; \$s/,$//" list2.js

echo "var rows = [" | cat - list2.js > list.js
echo -e "]\n" >> list.js

rm list2.js

# The list of available tag: dnf repoquery --querytags
#   name, arch, epoch, version, release, reponame (repoid), from_repo, evr,
#   debug_name, source_name, source_debug_name,
#   installtime, buildtime, size, downloadsize, installsize,
#   provides, requires, obsoletes, conflicts, sourcerpm,
#   description, summary, license, url, reason
# ---------------------------------------------------------------------------------
