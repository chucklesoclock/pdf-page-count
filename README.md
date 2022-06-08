# pdf-page-count
Counts all the pages of all the PDFs in a directory

## Usage 

### Without Python installation 

- place executable in directory you have the pdfs in
- run `pdf_page_counter.exe` in command prompt
- it should output total pages to screen
- view generated `pdf_page_counter.log` in a simple text editor for more detailed info

### With Python installation

- clone environment from file (TODO: add requirements file)
- place `pdf_page_counter.py` in directory 
- `python pdf_page_counter`
- total pages will be printed to screen
- view `pdf_page_counter.log` for more detailed info

## Gotchas/Roadmap

- the program will not walk down subdirectories looking for pdfs. functionality will be added in future release
- TODO: make into CLI with `click`
