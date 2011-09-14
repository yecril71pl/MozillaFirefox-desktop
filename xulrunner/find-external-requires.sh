#!/bin/sh
# Finds requirements provided outside of the current file set

filelist=$( sed "s/[]['\"*?{}]/\\\\\&/g" )
provides=$( echo "$filelist" | /usr/lib/rpm/find-provides )
echo "$filelist" \
    | /usr/lib/rpm/find-requires \
    | grep -F -v "$provides" \
    | sort -u
