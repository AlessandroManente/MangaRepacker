# ---- Config ----
APP_NAME = mangarepacker
VERSION = 0.0.1
MAIN_SCRIPT = src/app/main.py

LINUX_DIST = build/linux
WINDOWS_DIST = build/windows
DEB_DIR = build/deb
FLATPAK_DIR = build/flatpak

# ---- Targets ----
.PHONY: all linux windows flatpak clean deb appimage windows-installer

all:
ifeq ($(OS),Windows_NT)
	@$(MAKE) windows-installer
else
	@$(MAKE) linux flatpak deb appimage
endif

linux:
	@echo "🔧 Building Linux binary..."
	@mkdir -p $(LINUX_DIST)
	@pyinstaller --noconfirm --onefile --windowed \
		--name $(APP_NAME) \
		$(MAIN_SCRIPT) \
		--distpath $(LINUX_DIST)
	@echo "✅ Linux binary at $(LINUX_DIST)/$(APP_NAME)"

windows:
	@echo "🔧 Building Windows binary..."
	@mkdir -p $(WINDOWS_DIST)
	@pyinstaller --noconfirm --onefile --windowed \
		--name $(APP_NAME).exe \
		$(MAIN_SCRIPT) \
		--distpath $(WINDOWS_DIST)
	@echo "✅ Windows binary at $(WINDOWS_DIST)/$(APP_NAME).exe"

windows-installer: windows
	@echo "🛠️  Creating Windows installer with Inno Setup..."
	@iscc packaging/windows/installer.iss
	@echo "✅ Windows installer at build/windows/yourapp-setup.exe"

flatpak:
	@echo "📦 Building Flatpak..."
	@flatpak-builder --user --force-clean $(FLATPAK_DIR) packaging/flatpak/yourapp.json
	@echo "✅ Flatpak build complete"

deb: linux
	@echo "📦 Creating .deb package..."
	@mkdir -p build/deb/usr/bin
	@cp $(LINUX_DIST)/$(APP_NAME) build/deb/usr/bin/$(APP_NAME)
	@mkdir -p build/deb/DEBIAN
	@cp packaging/deb/control build/deb/DEBIAN/control
	@dpkg-deb --build build/deb build/$(APP_NAME).deb
	@echo "✅ .deb created: build/$(APP_NAME).deb"

clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf build/ dist/ __pycache__ .pytest_cache *.spec 
	@find . -type d -name '__pycache__' -exec rm -r {} +
	@echo "✅ Clean complete"
	
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