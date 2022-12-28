import csv
import json

test_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
]
with open("./test2.csv", "w") as f:
    cw = csv.writer(f)
    cw.writerow(test_list)




# load json file
with open("./test.json", "r") as f:
    j_info = json.loads(f.read())

# write csv file
with open("test.csv", "w") as f:
    fieldnames = ['nnc', 'input', 'output']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for j in j_info:
        writer.writerow(j)
        print(j)

# read csv file
with open("./test.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['nnc'])
        print(row['input'])
        print(row['output'])
