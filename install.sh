#!/bin/bash

mkdir -p database
sqlite3 database/trunk.db < scripts/bootstrap.sql

