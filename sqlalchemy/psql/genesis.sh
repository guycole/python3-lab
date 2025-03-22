#!/bin/bash
#
# Title:genesis.sh
# Description:
# Development Environment: OS X 12.7.6/postgres 15.8
#
psql -U postgres template1 (or psql -U gsc template1)

# (mac) user
createuser -U gsc -d -e -l -P -r -s lab_admin
woofwoof
createuser -U gsc -e -l -P lab_client
batabat

# (linux) su - postgres
createuser -U postgres -d -e -l -P -r -s lab_admin
woofwoof
createuser -U postgres -e -l -P lab_client
batabat

createdb pylab -O lab_admin -E UTF8 -T template0 -l C

# psql -h localhost -p 5432 -U lab_admin -d pylab
# psql -h localhost -p 5432 -U lab_client -d pylab
