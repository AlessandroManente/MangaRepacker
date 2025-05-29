# MangaRepacker

A project which aims to give a toolkit to manage and repack manga (and comics)
in .cbz.

This is meant to be an utility tool to help maintain a library managed through Kavita. This means that the expected files/folder structure would be as described [here](https://wiki.kavitareader.com/guides/scanner/).

## Features

- Cross-platform desktop interface

- Built using PySide6 (Qt for Python)

- Easy to contribute

Documentation [here](docs/index.md).

## Dependency

- Poetry

- If building on Linux:
  - Flatpak:  
  - dpkg

- If building on Windows:
  - InnoSetup

## Installation

```bash

make setup
make all

```

## Run tests

```bash

make setup
make run

```

## Tips

Remember to: 

```bash

export PATH="$HOME/.local/bin:$PATH"

```
