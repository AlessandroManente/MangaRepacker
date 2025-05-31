import zipfile
import rarfile
from PIL import Image
import os
import glob
import json
import modules.mangarepacker_single_stats as mpss
import numpy as np
import time
import jsonpickle

class MangaRepackerStats:

    def __init__(self):
        self.folder = ''
        self.number_of_files = 0
        self.medium_number_of_pages_per_file = 0
        self.median_number_of_pages_per_file = 0
        self.min_number_of_pages = 0
        self.max_number_of_pages = 0
        self.number_of_white_pages = 0
        self.number_of_missing_comicinfo = 0
        # self.number_of_dupliacated_pages = 0
        self.stats_files = {}
        # self.duplicated_pages = {}

    def __str__(self):
        return f"MangaRepackerStats instance"

    def get_folder_stats(self, folder: str) -> str:
        print(folder)
        txt_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".cbz"):
                    txt_files.append(os.path.join(root, file))
        txt_files.sort()

        pages_number = []
        white_pages = 0
        missing_comic_info = 0
        stats_files = {}
        for file in txt_files:
            stats = mpss.MangaRepackerSingleStats()
            start = time.process_time()
            end = time.process_time()
            print(file, ":", (end - start) * 1e3, "ms")
            stats.analyze_single_file(file)
            self.stats_files[file] = stats
            #
            pages_number.append(len(stats.pages_stats.keys()))
            white_pages += stats.get_number_blank_pages()
            missing_comic_info += stats.get_number_missing_comic_info()

        self.folder = folder
        self.number_of_files = len(txt_files)
        self.medium_number_of_pages_per_file = int(np.average(pages_number))
        self.median_number_of_pages_per_file = int(np.median(pages_number))
        self.min_number_of_pages_per_file = int(np.min(pages_number))
        self.max_number_of_pages_per_file = int(np.max(pages_number))
        self.number_of_white_pages = white_pages
        self.number_of_missing_comicinfo = missing_comic_info

        return json.dumps(self, default=vars)
