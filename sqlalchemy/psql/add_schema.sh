#!/bin/bash
#
# Title:add_schema.sh
# Description:
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
# psql -U lab_admin -d pylab
#
export PGDATABASE=pylab
export PGHOST=localhost
export PGPASSWORD=woofwoof
export PGUSER=lab_admin
#
psql < table1.psql
psql < table2.psql
#
