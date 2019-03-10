import os
import csv

csv_path = os.path.join("Resources","budget_data.csv")

with open(csv_path,newline="") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	csv_header = next(csv_reader)

	# count the number of rows in the csv
	row_count = sum(1 for row in csv_reader)

	# set the starting value of net profit/loss as 0
	start_total = 0


	# add the net profit/loss row by row with for loop
	for row in csv_reader:
		total = float(start_total) + float(row[1])
		start_total = float(total)

	
	print(f"Total Months: {row_count}")
	print(f"Total Net Profit/Loss: ${total}")