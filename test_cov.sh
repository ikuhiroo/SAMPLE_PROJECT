#!/bin/bash

py.test && flake8 . --config=flake8_config
