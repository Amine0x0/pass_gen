#!/bin/bash

# Install pip if not present
if ! command -v pip &> /dev/null; then
    echo "Installing pip..."
    
    # Download get-pip.py
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

    # Install pip
    python3 get-pip.py
    
    # Clean up
    rm get-pip.py
fi

# Install required packages using pip
pip install -r requirements.txt

echo "Requirements installed successfully."

