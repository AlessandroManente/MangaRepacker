import zipfile
import rarfile
from PIL import Image
import os
import glob
import json


class MangaRepacker:

    def __init__(self):  # , par1, par2):
        pass
        # self.par1 = par1
        # self.par2 = par2

    def __str__(self):
        return "MangaRepacker instance"

    def load_cbz_to_memory(cbz_bytes) -> dict:
        image_dict = {}
        metadata = None

        with zipfile.ZipFile(io.BytesIO(cbz_bytes), "r") as zf:
            for name in zf.namelist():
                if name.lower().endswith((".jpg", ".jpeg", ".png")):
                    image_dict[name] = Image.open(io.BytesIO(zf.read(name))).copy()
                elif name == "ComicInfo.xml":
                    metadata = zf.read(name).decode("utf-8")

        cbz_file = {}
        cbz_file["pages"] = image_dict
        cbz_file["metadata"] = metadata

        return cbz_file

    def load_cbz_to_memory_from_file(filename: str) -> dict:
        with open(filename, "rb") as f:
            cbz_bytes = f.read()
        return load_cbz_to_memory(cbz_bytes)

    def cbz_file_stat(filename: str) -> dict:
        cbz_file = load_cbz_to_memory_from_file(filename)

        cbz_stats = {}
        cbz_stats["n_pages"] = cbz_file["pages"].length
        cbz_stats["md_present"] = cbz_file["metadata"] is None

        return cbz_stats

    def folder_stats(folder: str) -> str:
        print(folder)
        txt_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".cbz"):
                    txt_files.append(os.path.join(root, file))
        txt_files.sort()

        stats_files = []

        return json.dumps(txt_files)
