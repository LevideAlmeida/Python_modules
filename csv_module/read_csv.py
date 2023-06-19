"""
csv to read .csv files
"""
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "Exemple-File.csv"

with open(CSV_PATH, "r") as csv_file:
    # read csv_file with csv.reader
    reader = csv.reader(csv_file)
    print(reader)

    for line in reader:
        print(line)

    # read csv_file as dict
    dict_reader = csv.DictReader(csv_file)

    for line in dict_reader:
        print(line['NAME'], line['AGE'], line['FAVORITE COLOR'])
