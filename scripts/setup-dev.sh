#!/bin/bash
echo "Setting up Python environment with Poetry..."
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry install

echo "Setting up Flatpak SDK..."
./scripts/setup-flatpak.sh

echo "Done! Run 'make run' or 'make flatpak-run' to start."