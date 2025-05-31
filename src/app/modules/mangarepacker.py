import zipfile
import rarfile
from PIL import Image
import os
import glob
import json
import modules.mangarepacker_stats as mps

class MangaRepacker:

    def __init__(self):
        pass

    def __str__(self):
        return f"MangaRepacker instance"

    def folder_stats(folder: str) -> str:
        stats = mps.MangaRepackerStats()
        json_data = stats.get_folder_stats(folder)

        return json_data
