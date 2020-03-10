# csv-merge
Merges two CSV-files where the specific given colum values are identical

## Usage
The usage is simple. Just call the script with python and give him your input files. Then you give him the colum index where the match should be

### Help
```bash
usage: mergecsv.py [-h] -i INPUTFILE -m MATCH [-o OUTPUTFILE] [-d DELIMITER]
                   [-v]

Merges two CSV files

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputFile INPUTFILE
                        Path of the InputFile
  -m MATCH, --match MATCH
                        The index of the CSV File columns which should match
                        for merging
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        Path of the OutputFile
  -d DELIMITER, --delimiter DELIMITER
                        Path of the OutputFile
  -v, --verbose         Prints output on both stdout and in file
```