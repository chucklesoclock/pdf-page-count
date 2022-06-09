# pdf-page-count
Counts all the pages of all the PDFs in a directory

## Usage

```
$ python pdf_page_counter.py --help
Usage: pdf_page_counter.py [OPTIONS] [DIR_PATH]

Options:
  -r, --recursive  recursive search; count all pdfs in all subdirectors of
                   DIR_PATH
  -t, --table      print a table to terminal using rich
  --help           Show this message and exit.
```

### Without Python installation 

- run `pdf_page_counter.exe` in command prompt

### With Python installation

- create conda environment with `conda env create -f environment.yml`
- `python pdf_page_counter.py`

### Log File

- view `pdf_page_counter.log` in text editor for more detailed info. PDF read errors will be populated here. 
