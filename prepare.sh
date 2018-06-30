#!/bin/bash

BASE_DIR=`dirname ${0}`
pip install -r "${BASE_DIR}"/requirements.txt
pip install -e .
