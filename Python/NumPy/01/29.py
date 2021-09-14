import csv

with open("student.csv", "r") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
for item in rows:
    print(item)
