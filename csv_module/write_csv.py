"""
csv to write in .csv files
"""
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "Exemple-File2.csv"

teachers_list = [
    {'name': 'Wilker', 'age': '45', 'subject': 'math'},
    {'name': 'Ricardo', 'age': '35', 'subject': 'history'},
    {'name': 'Fernando', 'age': '60', 'subject': 'chemical'},
]

with open(CSV_PATH, 'w') as file:
    columns_name = teachers_list[0].keys()
    # create a writer with csv.writer
    writer = csv.writer(file)
    # using the writer to write in the file
    writer.writerow(columns_name)

    # write all teachers_list values in the file
    for teacher in teachers_list:
        writer.writerow(teacher.values())

    # write dicts in csv_file
    dict_writer = csv.DictWriter(file, fieldnames=columns_name)

    dict_writer.writeheader()  # To write columns_name

    # write the dicts in teachers_list
    for teacher in teachers_list:
        writer.writerow(teacher.values())
