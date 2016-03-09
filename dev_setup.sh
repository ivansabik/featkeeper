#!/bin/bash
sudo apt-get update
sudo apt-get install git python python-pip python-all-dev mongodb nodejs python-virtualenv
sudo apt-get install npm
npm install -g grunt-cli
git clone https://github.com/ivansabik/featkeeper
cd featkeeper
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
npm install
grunt
