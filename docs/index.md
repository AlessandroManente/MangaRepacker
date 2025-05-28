# MangaRepacker Wiki

## Features

- [ ] An app split into (a CLI (C) and) a GUI (G) app (maybe [both](https://stackoverflow.com/a/2857700) (B))
- [ ] The app will have the following functions:
  - [ ] (B) Merge multiple .cbz/.cbr files:
    - [ ] Into one *mega* file
    - [ ] Into multiple files by a fixed number of files
    - [ ] Into multiple files by a given list of chapters
  - [ ] (B) Split multiple .cbz/.cbr files:
    - [ ] Into multiple files by a fixed number of pages
    - [ ] Into multiple files by a given list of number of pages
    - [ ] Into a specified number of files
  - [ ] (B) Find duplicate pages in a given set of files and let the user choose to delete them all or keep a copy of one or multiple
  - [ ] (B) Add page in a specified position of a file (default beginning/end)
  - [ ] (G) Show a preview of the pages of the file and let the user select any quantity and delete them
  - [ ] (B) Return statistics on the files, like:
    - [ ] Number of files
    - [ ] Medium number of pages per file
    - [ ] Median number of pages per file
    - [ ] Min number of pages per file
    - [ ] Max number of pages per file
  - [ ] (B) Return a list of files with higher than medium/median number of pages per file
  - [ ] (B) Delete pages above medium/median number of pages per file
    - [ ] (B) Ask to choose per file the exact page
    - [ ] (G) Show a preview of the last page to be kept and the first to be deleted
  - [ ] (B) Batch edit of `comic_info.xml`

By default the merging should edit the `comic_info.xml` such that it calls the new files volumes.

By default the splitting should edit the `comic_info.xml` such that it calls the new files chapters.
