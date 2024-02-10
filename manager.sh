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
    CODESPACE_URI="https://${CODESPACE_NAME}-8000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
    if [ CODESPACE_URI != "https://-8000." ]; then
        echo "Auto detected codespace URI: ${CODESPACE_URI}"
    fi

    source .venv/bin/activate
    if [ "$2" == "" ]; then
        export BASE_URI=$CODESPACE_URI
    else
        export BASE_URI=$2
    fi
    echo "Using URI: ${BASE_URI}"
    uvicorn app.web:app --host 0.0.0.0
else
    echo "Invalid argument"
    echo "Use 'install' or 'run'"
fi 