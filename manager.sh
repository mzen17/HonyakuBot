#!/bin/bash
# Runs/Installs app

if [ "$1" == "install" ]; then
    if [ ! -d ".venv" ]; then
        echo "Creating virtual environment"
    else
        echo "Virtual environment already exists"
        echo "Use 'rm .venv' to remove it"
        exit 1
    fi
    source .venv/bin/activate
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    pip install sentence-transformers

elif [ "$1" == "run" ]; then
    if [ ! -d ".venv" ]; then
        echo "Virtual environment does not exist"
        echo "Use 'install' to create it"
        exit 1
    fi
    source .venv/bin/activate
    python3 app/main.py 

else
    echo "Invalid argument"
    echo "Use 'install' or 'run'"
fi 