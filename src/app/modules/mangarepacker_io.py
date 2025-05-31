import zipfile
import rarfile
from PIL import Image
import os
import glob
import json
import io

class MangaRepackerIOPage:

    def __init__(self):
        self.filename = ''
        self.image = None

    def __str__(self):
        return f"MangaRepackerIOPage instance"

class MangaRepackerIO:

    def __init__(self):
        self.filename = ''
        self.pages = {}
        self.comic_info = None

    def __str__(self):
        return f"MangaRepackerIO instance"

    def load_cbz_to_memory(self, cbz_bytes) -> bool:
        image_dict = {}
        metadata = None

        with zipfile.ZipFile(io.BytesIO(cbz_bytes), "r") as zf:
            for name in zf.namelist():
                if name.lower().endswith((".jpg", ".jpeg", ".png")):
                    page = MangaRepackerIOPage()
                    page.filename = name
                    page.image = Image.open(io.BytesIO(zf.read(name))).copy()
                    image_dict[name] = page
                elif name == "ComicInfo.xml":
                    metadata = zf.read(name).decode("utf-8")

        self.pages = image_dict
        self.comic_info = metadata

        return True

    def load_cbz_to_memory_from_file(self, filename: str) -> bool:
        with open(filename, "rb") as f:
            cbz_bytes = f.read()
        self.filename = filename

        return self.load_cbz_to_memory(cbz_bytes)
