# Makefile
setup:
 ./scripts/setup-dev.sh

run:
 poetry run python src/app/main.py

flatpak-run:
 flatpak-builder --run build-dir flatpak/app.json rapp

flatpak-install:
 flatpak-builder --user --install --force-clean build-dir flatpak/app.json

test:
 poetry run pytest tests/