#!/bin/bash

apt update
apt install python-virtualenv python-stdeb python-pbr

DEB_BUILD_OPTIONS=nocheck python setup.py --command-packages=stdeb.command sdist_dsc --depends "python-pbr, python-dateutil" bdist_deb

