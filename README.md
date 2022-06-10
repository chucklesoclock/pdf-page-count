# pdf-page-count
Counts all the pages of all the PDFs in a directory. A very specific tool for a very specific task which burdened my partner. 

## Usage

```
$ python pdf_page_counter.py --help
Usage: pdf_page_counter.py [OPTIONS] [DIR_PATH]

  Count all the PDFs in the directory DIR_PATH.

Options:
  -r, --recursive  recursive search; count all pdfs in all subdirectors of
                   DIR_PATH
  -t, --table      print a table to terminal using rich library
  --help           Show this message and exit.
```

### On Windows

#### Powershell

- `.\pdf_page_counter.exe`

#### Command Prompt

- `pdf_page_counter.exe`

### With Python installation

- create conda environment with `conda env create -f environment.yml`
- `python pdf_page_counter.py`

### Log File

- view `pdf_page_counter.log` in text editor for more detailed info. PDF read errors will be populated there. 

## Acknowledgements

Many thanks to the [rich](https://github.com/Textualize/rich) library for their excellent terminal printing functionality. 
