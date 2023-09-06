#!/bin/bash

for Files in ./*
do
    if [ -d $Files/.git ];
    then
	echo "Updating $Files directory / git"
	cd $Files
	git pull
	git submodule init
	git submodule update
	cd ..
    fi

    if [ -d $Files/.svn ];
    then
	echo "Updating $Files directory / svn"
	cd $Files
	svn update
	cd ..
    fi

    if [ -d $Files/CVS ];
    then
	echo "Updating $Files directory / cvs"
	cd $Files
	cvs update
	cd ..
    fi

    if [ -d $Files/.hg ];
    then
	echo "Updating $Files directory / hg"
	cd $Files
	hg pull
	cd ..
    fi

    if [ -d $Files/.bzr ];
    then
	echo "Updating $Files directory / bzr"
	cd $Files
	bzr pull
	cd ..
    fi
done

	  
