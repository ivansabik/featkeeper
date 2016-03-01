#!/bin/bash
git clone https://github.com/ivansabik/featkeeper
cd featkeeper
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
