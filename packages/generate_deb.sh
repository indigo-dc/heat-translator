#!/bin/bash

python setup.py --command-packages=stdeb.command sdist_dsc --depends "python-pbr, python-dateutil" bdist_deb

