#!/usr/bin/env bash

set -e

echo "Starting DemoCopilotAgents setup..."

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Running application..."
python main.py

echo ""
echo "Running tests..."
pytest -v

echo ""
echo "Demo setup and execution completed successfully."
#chmod +x run_demo.sh
#./run_demo.sh