#!/bin/bash

# Create a temporary directory to install the packages into
mkdir temp

# Install the dependencies specified in the requirements.txt file
pip install -r ./requirements.txt -t ./temp --no-user

# Change into the temporary directory
cd temp

# Zip the packages into a file named "lambda-layer.zip"
zip -r lambda-layer.zip .

# Move the zip file to the parent directory
mv lambda-layer.zip ..

# Clean up the temporary directory
cd ..
rm -rf temp
