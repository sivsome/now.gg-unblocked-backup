#!/bin/bash

# Run the existing commands
chmod +x caddy
./caddy run --config ./Caddyfile &

# Run the Python script
python3 errorspoof.py
