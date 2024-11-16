#!/bin/bash
#
# Title: verify_all.sh
# Description: basic sanity check
# Development Environment: macOS Monterey 12.6.9
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
set -e
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
  /usr/bin/unzip -q $file_name 
  python /Users/gsc/Documents/github/python3-lab/choral_wave/verifier.py $file_name
done < /tmp/allzip
#
/bin/rm -rf choral_wave
