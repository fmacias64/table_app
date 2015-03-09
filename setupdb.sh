#! /usr/bin/env bash

. "env.sh"

dropdb --if-exists $DBNAME
createdb $DBNAME
echo $DBNAME
psql $DBNAME < schema.sql
