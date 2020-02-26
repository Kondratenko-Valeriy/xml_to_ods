# Parsing XML and saving data to Open Document Spreadsheet file
Script parses XML files from the directory 'xml' and save data to ODS files to the directory 'ods'. 
Designed for OS Windows, but not tested on it :)
 
## Requirements:
1. Download ans install latest Python 3 version (3.7+):\
    https://www.python.org/downloads/windows  
    https://docs.python.org/3.8/using/windows.html
    
2. Install Python packages:
- BeautifulSoup - parsing XML files: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
- pyexcel-ods - writing data to ODS files: https://github.com/pyexcel/pyexcel-ods
- tqdm - progress bar output: https://github.com/tqdm/tqdm#installation
- transliterate - internal transliterating cyrillic tags/attributes: https://github.com/barseghyanartur/transliterate#installation

## Script running:
Open Command line: Start menu -> Run and type cmd.
```console

C:\Users\YourName> py script_directory\xml_to_ods.py

```
https://docs.python.org/3/faq/windows.html#id2
