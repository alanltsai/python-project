import os
import csv

csv_path = os.path.join("Resources","budget_data.csv")

def average(list):
    sum(list) / len(list)
    
with open(csv_path,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Set start variables for count
    start_row_count = 0
    start_total = 0

    for row in csv_reader:
    	# Problem 1 
        # row_count = start_row_count + 1
        # start_row_count = row_count

        # Problem 2
        total = float(start_total) + float(row[1])
        start_total = float(total)

print(row_count)
print(total)