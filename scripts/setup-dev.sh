#!/bin/bash
echo "Setting up Python environment with Poetry..."
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry install --no-root

if [[ "$(uname)" == "Linux" ]]; then
    echo "Setting up Flatpak SDK..."
    ./scripts/setup-flatpak.sh
else
    echo "Flatpak setup is skipped. This is not a Linux system."
    winget install -e --id JRSoftware.InnoSetup
    echo "Innosetup installed. Please add ISCC to PATH"
fi

echo "Done! Run 'make run' or 'make flatpak-run' to start."