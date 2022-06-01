#!/bin/sh
mkdir YOUTUBE_CRAWLING
cd YOUTUBE_CRAWLING
git pull "https://github.com/ospTEAM4/OSP_TERM.git"
sudo apt-get install virtualenv
sudo apt-get install pip
virtualenv -p python3 venv
source venv/bin/activate
