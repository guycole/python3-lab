#!/bin/bash
#
# Title: verifier.sh
# Description: 
# Development Environment: macOS Monterey 12.6.9
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
TARGET=/Users/gsc/Documents/audio-s3sync/choral/wave/a/ac_dc/back_in_black.zip
#
/bin/rm -rf choral_wave
/usr/bin/unzip $TARGET
#
if test -f choral_wave/manifest.xml
then
  source venv/bin/activate
  python ./verifier.py
  exit 0
else
  echo "manifest.xml missing"
  exit 1
fi
#
