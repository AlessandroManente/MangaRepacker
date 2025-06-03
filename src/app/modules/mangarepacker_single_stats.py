import zipfile
import rarfile
from PIL import Image
import os
import glob
import json
import modules.mangarepacker_io as mpio
import numpy as np
import hashlib
import io


class MangaRepackerPageStats:

    def __init__(self):
        self.filename = ""
        self.is_blank = False
        self.hash = ""

    def __str__(self):
        return f"MangaRepackerPageStats instance"

    def to_dict(self):
        return {
            "filename": self.filename,
            "is_blank": self.is_blank,
            "hash": self.hash,
        }


class MangaRepackerSingleStats:

    def __init__(self):
        self.filename = ""
        self.comic_info_present = False
        self.pages_stats = {}

    def __str__(self):
        return f"MangaRepackerSingleStats instance"

    def to_dict(self):
        return {
            "filename": self.filename,
            "comic_info_present": self.comic_info_present,
            "pages_stats": [stat.to_dict() for stat in self.pages_stats.values()],
        }

    def is_image_all_white(self, img):
        img = img.convert("RGB")
        arr = np.array(img)
        return bool(np.all(arr == 255))

    def hash_image(self, image: Image.Image, method='sha256') -> str:
        hasher = hashlib.new(method)
        with io.BytesIO() as output:
            image.save(output, format='PNG')
            hasher.update(output.getvalue())
        return hasher.hexdigest()

    def analyze_single_file(self, filename: str):
        cbz_file = mpio.MangaRepackerIO()
        cbz_file.load_cbz_to_memory_from_file(filename)
        self.filename = filename
        self.comic_info_present = cbz_file.comic_info != ''
        if bool(cbz_file.pages):
            for cbz_page_name in cbz_file.pages:
                cbz_page = cbz_file.pages[cbz_page_name]
                page = MangaRepackerPageStats()
                page.filename = cbz_page.filename
                if not (cbz_page.image is None):
                    page.hash = self.hash_image(cbz_page.image)
                    page.is_blank = self.is_image_all_white(cbz_page.image)
                self.pages_stats[cbz_page_name] = page

    def get_number_blank_pages(self) -> int:
        n_blanks = 0
        for page_name in self.pages_stats:
            page = self.pages_stats[page_name]
            if page.is_blank:
                n_blanks + 1

        return n_blanks

    """
    def get_number_missing_comic_info(self) -> int:
        n_missing = 0
        for page_name in self.pages_stats:
            page = self.pages_stats[page_name]
            if not page.comic_info_present:
                n_missing + 1
                
        return n_missing
    """
