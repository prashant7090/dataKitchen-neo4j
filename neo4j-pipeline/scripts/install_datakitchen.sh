#!/bin/bash

# Install pipx if not already installed
python3 -m pip install --upgrade pip
python3 -m pip install pipx

# Ensure pipx path is set (especially in Docker)
export PATH="$PATH:/root/.local/bin"

# Install DataKitchen CLI
pipx install datakitchen