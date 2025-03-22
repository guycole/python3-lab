#!/bin/bash
#
# Title:drop_schema.sh
# Description: remove schema
# Development Environment: OS X 10.15.2/postgres 12.12
# Author: G.S. Cole (guy at shastrax dot com)
#
export PGDATABASE=pylab
export PGHOST=localhost
export PGPASSWORD=woofwoof
export PGUSER=lab_admin
#
psql $PGDATABASE -c "drop table table2"
psql $PGDATABASE -c "drop table table1"
#
