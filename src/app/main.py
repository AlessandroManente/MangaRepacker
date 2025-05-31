import modules.mangarepacker as mp

def main():
    MangaRep = mp.MangaRepacker
    print(MangaRep)
    print(MangaRep.folder_stats('/home/alessandro/_temp/20th Century Boys/'))

if __name__ == "__main__":
    main()