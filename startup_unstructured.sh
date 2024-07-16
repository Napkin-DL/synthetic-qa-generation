#!/bin/bash

sudo apt-get install software-properties-common -y
sudo add-apt-repository ppa:alex-p/tesseract-ocr5 -y
sudo apt-get update -y
sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-eng tesseract-ocr-kor -y
sudo apt-get install libgl1-mesa-glx libglib2.0-0 -y
sudo apt install libreoffice -y
pip install -U "unstructured[all-docs]"
pip install -r requirements.txt