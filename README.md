# MangaRepacker

A project which aims to give a toolkit to manage and repack manga (and comics)
in .cbz.

## Features

- Cross-platform desktop interface

- Built using PySide6 (Qt for Python)

- Easy to contribute

## Dependency

- Poetry:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

- If building on Linux:
  - Flatpak:

    ```bash
    ./scripts/setup-flatpak.sh
    ```

## Installation

```bash

pip install -r requirements.txt

python src/your_app/main.py

```

## Run tests

```bash

make setup
make run

```
