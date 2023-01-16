#!/bin/bash

# Setup and install dependencies
sudo apt-get update
sudo apt-get install -y git python3 python3-pip python3-venv
sudo apt-get install build-essential portaudio19-dev python3.10-dev

# Install virtual environment
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
