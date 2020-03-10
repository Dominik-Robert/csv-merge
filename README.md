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

### Example
Here is an Example with the files under Example/

```bash
python3.7 mergecsv.py -i Example/first.csv -i Example/second.csv -i Example/third.csv -m 0 -m 0 -m 0

# Matches the column index 0 in all files. Which means that this is the key for the comparison of the merge
```
