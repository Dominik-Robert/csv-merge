import argparse
import csv

parser = argparse.ArgumentParser(description='Merges two CSV files')
parser.add_argument("-i", "--inputFile", action="append", type=str, required=True, help="Path of the InputFile")
parser.add_argument("-m", "--match", action="append", type=int, required=True, help="The index of the CSV File columns which should match for merging")
parser.add_argument("-o", "--outputFile", default='merged.csv', type=str, help="Path of the OutputFile")
parser.add_argument("-d", "--delimiter", default=';', type=str, help="Path of the OutputFile")
parser.add_argument("-v", "--verbose", action="store_true", help="Prints output on both stdout and in file")

args = parser.parse_args()
inputFiles = args.inputFile
matches = args.match


output = open(args.outputFile, "a")

with open(inputFiles[0]) as firstFile:
  firstCSV = csv.reader(firstFile, delimiter=args.delimiter)
  for row in firstCSV:
    insert = ";".join(row)

    for index in range(len(inputFiles)):
      if index == 0:
        continue
      with open(inputFiles[index]) as otherFile:
        otherCSV = csv.reader(otherFile, delimiter=args.delimiter)
        for matchData in otherCSV:
          if row[matches[0]] == matchData[matches[index]]:
            insert += ";" + ";".join(matchData[:matches[index]]) + ";".join(matchData[matches[index]+1:])
            break
    if args.verbose:
      print(insert)
    output.write(insert + "\n")

output.close()