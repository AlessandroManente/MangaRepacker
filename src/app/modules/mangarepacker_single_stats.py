import zipfile
import rarfile
from PIL import Image
import os
import glob
import json
import modules.mangarepacker_io as mpio
import numpy as np

class MangaRepackerPageStats:

    def __init__(self):
        self.filename = ''
        self.is_blank = False
        self.hash = ''

    def __str__(self):
        return f"MangaRepackerPageStats instance"

class MangaRepackerSingleStats:

    def __init__(self):
        self.filename = ''
        self.comic_info_present = False
        self.pages_stats = {}

    def __str__(self):
        return f"MangaRepackerSingleStats instance"

    def is_image_all_white(self, img):
        img = img.convert("RGB")
        arr = np.array(img)
        return np.all(arr == 255)

    def analyze_single_file(self, filename: str):
        cbz_file = mpio.MangaRepackerIO()
        cbz_file.load_cbz_to_memory_from_file(filename)
        self.filename = filename
        self.comic_info_present = cbz_file.comic_info is None
        for cbz_page_name in cbz_file.pages:
            cbz_page = cbz_file.pages[cbz_page_name]
            page = MangaRepackerPageStats()
            page.filename = cbz_page.filename
            page.hash = cbz_page.image.__hash__
            page.is_blank = self.is_image_all_white(cbz_page.image)
            self.pages_stats[cbz_file.filename] = page

    def get_number_blank_pages(self) -> int:
        n_blanks = 0
        for page in self.pages_stats:
            if page.is_blank:
                n_blanks + 1
                
        return n_blanks

    def get_number_missing_comic_info(self) -> int:
        n_missing = 0
        for page in self.pages_stats:
            if not page.comic_info_present:
                n_missing + 1
                
        return n_missing