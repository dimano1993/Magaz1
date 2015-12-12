#!/bin/bash

set -e

#run unittests
./manage.py test

#test code style
py.test --pep8
