#!/bin/bash

# ./traverso-source.sh <tag>
# ./traverso-source.sh master

git clone https://git.savannah.nongnu.org/git/traverso.git
cd traverso
git checkout $1
if [ $? == 1 ]; then
    echo "Wrong branch / tag name: $1"
    exit 1
fi
find . -name .git -exec rm -rf {} \;
cd ..
tar cvfz traverso.tar.gz traverso
rm -rf traverso
