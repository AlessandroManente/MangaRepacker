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
        self.folder = ""
        self.number_of_files = 0
        self.medium_number_of_pages_per_file = 0
        self.median_number_of_pages_per_file = 0
        self.min_number_of_pages_per_file = 0
        self.max_number_of_pages_per_file = 0
        self.number_of_white_pages = 0
        self.number_of_missing_comicinfo = 0
        self.number_of_duplicated_pages = 0
        self.stats_files = {}
        self.duplicated_pages = {}

    def __str__(self):
        return f"MangaRepackerStats instance"

    def to_dict(self):
        return {
            "folder": self.folder,
            "number_of_files": self.number_of_files,
            "medium_number_of_pages_per_file": self.medium_number_of_pages_per_file,
            "median_number_of_pages_per_file": self.median_number_of_pages_per_file,
            "min_number_of_pages_per_file": self.min_number_of_pages_per_file,
            "max_number_of_pages_per_file": self.max_number_of_pages_per_file,
            "number_of_white_pages": self.number_of_white_pages,
            "number_of_missing_comicinfo": self.number_of_missing_comicinfo,
            "stats_files": [stat.to_dict() for stat in self.stats_files.values()],
            "duplicated_pages": self.duplicated_pages,
            "number_of_duplicated_pages": self.number_of_duplicated_pages,
        }

    def get_duplicated_pages(self):
        hashed_pages = {}
        for stat in self.stats_files.values():
            for page_hash in stat.pages_stats.keys():
                page = stat.pages_stats[page_hash]
                hashed_pages.setdefault(page.hash, []).append(stat.filename + '/' + page.filename)

        for page_hash in hashed_pages.keys():
            list_pages = hashed_pages[page_hash]
            duplicates = len(list_pages)
            if duplicates > 1:
                self.number_of_duplicated_pages += duplicates
                self.duplicated_pages[page_hash] = list_pages

        pass

    def get_folder_stats(self, folder: str) -> str:
        print(folder)
        start = time.process_time()
        txt_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".cbz"):
                    txt_files.append(os.path.join(root, file))
        txt_files.sort()
        end = time.process_time()
        print("list files:", (end - start) * 1e3, "ms")

        pages_number = []
        white_pages = 0
        missing_comic_info = 0
        for file in txt_files:
            start = time.process_time()
            stats = mpss.MangaRepackerSingleStats()
            stats.analyze_single_file(file)
            self.stats_files[file] = stats
            #
            pages_number.append(len(stats.pages_stats.keys()))
            white_pages += stats.get_number_blank_pages()
            if not stats.comic_info_present:
                missing_comic_info += 1

            end = time.process_time()
            print(file, ":", (end - start) * 1e3, "ms")
            
        self.folder = folder
        self.number_of_files = len(txt_files)
        self.medium_number_of_pages_per_file = int(np.average(pages_number))
        self.median_number_of_pages_per_file = int(np.median(pages_number))
        self.min_number_of_pages_per_file = min(pages_number)
        self.max_number_of_pages_per_file = max(pages_number)
        self.number_of_white_pages = white_pages
        self.number_of_missing_comicinfo = missing_comic_info
        self.get_duplicated_pages()

        return json.dumps(self.to_dict(), indent=2)
