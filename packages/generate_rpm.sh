#!/bin/bash

yum install python-pbr python-virtualenv rpm-build

echo "%_unpackaged_files_terminate_build 0" > ~/.rpmmacros
python setup.py bdist_rpm --requires="python-pbr, python-cliff, PyYAML, python-dateutil, python-six, python-keystoneclient, python-novaclient, python-glanceclient, python-heatclient, python-neutronclient, python-requests, tosca-parser"

