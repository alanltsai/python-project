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
    start_change = 0

    for row in csv_reader:
    	print(next(csv_reader[1]))


    # print(total_change)