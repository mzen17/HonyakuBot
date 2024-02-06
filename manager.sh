#!/bin/bash
# Runs/Installs app

echo "This script should be running in repository directory."

if [ "$1" == "install" ]; then
    if [ ! -d ".venv" ]; then
        echo "Creating virtual environment"
        python -m venv .venv
    else
        echo "Virtual environment already exists"
        echo "Use 'rm .venv' to remove it"
        exit 1
    fi
    source .venv/bin/activate
    pip install -r torchreqs.txt
    pip install -r webreqs.txt
    mkdir static

elif [ "$1" == "run" ]; then
    if [ ! -d ".venv" ]; then
        echo "Virtual environment does not exist"
        echo "Use 'install' to create it"
        exit 1
    fi
    echo "If the URL does not root to /, enter base URI into second paramater."
    echo "Format for that is /base_uri"

    source .venv/bin/activate
    export BASE_URI=$2
    uvicorn app.web:app --host 0.0.0.0
else
    echo "Invalid argument"
    echo "Use 'install' or 'run'"
fi 