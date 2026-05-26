Write-Host "Starting DemoCopilotAgents setup..."

if (-Not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
& .\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Running application..."
python main.py

Write-Host ""
Write-Host "Running tests..."
pytest -v

Write-Host ""
Write-Host "Demo setup and execution completed successfully."
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#.\run_demo.ps1 