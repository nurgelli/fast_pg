#!/bin/sh

export PGUSER='nurgelli'


psql -c "CREATE DATABASE postgres_db"

psql postgres_db -c "CREATE EXTENSION IF NOT EXITS \"uuid-ossp\";"


