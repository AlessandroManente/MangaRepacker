import modules.mangarepacker as mp

def main():
    MangaRep = mp.MangaRepacker
    stats = MangaRep.folder_stats('/home/alessandro/_temp/6000/')
    with open("output.json", "w", encoding="utf-8") as f:
        f.write(stats)
    # print(stats)

if __name__ == "__main__":
    main()