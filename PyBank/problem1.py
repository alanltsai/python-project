import os
import csv

csv_path = os.path.join("Resources","budget_data.csv")

def average(list):
	sum(list) / len(list)

with open(csv_path,newline="") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	csv_header = next(csv_reader)

	# Problem 1
	# count the number of rows in the csv
	# row_count = sum(1 for row in csv_reader)
	start_row_count = 0

	for row in csv_reader:
		row_count = start_row_count + 1
		start_row_count = row_count

	print(row_count)