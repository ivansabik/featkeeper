#!/bin/bash
sudo apt-get install git python python-pip python-all-dev mongodb-org
git clone https://github.com/ivansabik/featkeeper
cd featkeeper
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python -m unittest discover
