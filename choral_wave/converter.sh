#!/bin/bash
#
# Title: converter.sh
# Description: create manifest.json
# Development Environment: macOS Monterey 12.6.9
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ROOT_DIR=/Users/gsc/Documents/audio-s3sync/choral/wave
#
source venv/bin/activate
#
pushd $ROOT_DIR
/usr/bin/find . -name *.zip > /tmp/allzip
#
while read -r file_name; do
  /bin/rm -rf choral_wave
  echo "$file_name"
  /usr/bin/unzip $file_name
  if test -f choral_wave/manifest.json
  then
    echo "manifest.json noted"
  else
    echo "manifest.json missing"
    python /Users/gsc/Documents/github/python3-lab/choral_wave/converter.py $file_name
    mv manifest.json choral_wave
    zip temp choral_wave/*
    mv temp.zip $file_name
  fi
done < /tmp/allzip

/bin/rm -rf choral_wave
