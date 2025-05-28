# MangaRepacker Wiki

## Features

- [ ] An app split into (a CLI and) a GUI app (maybe [both](https://stackoverflow.com/a/2857700))
- [ ] The app will have the following functions:
  - [ ] Merge multiple .cbz/.cbr files:
    - [ ] Into one *mega* file
    - [ ] Into multiple files by a fixed number of files
    - [ ] Into multiple files by a given list of chapters
  - [ ] Split multiple .cbz/.cbr files:
    - [ ] Into multiple files by a fixed number of pages
    - [ ] Into multiple files by a given list of number of pages
    - [ ] Into a specified number of files
  - [ ] Find duplicate pages in a given set of files and let the user choose to delete them all or keep a copy of one or multiple
  - [ ] Add page in a specified position of a file (default beginning/end)

By default the merging should edit the `comic_info.xml` such that it calls the new files volumes.

By default the splitting should edit the `comic_info.xml` such that it calls the new files chapters.
