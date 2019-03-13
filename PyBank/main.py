import os
import csv

csv_path = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Output","Bank_Results.txt")

def average(list):
    sum(list) / len(list)
    
with open(csv_path,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Set start variables for count
    start_row_count = 0
    start_total = 0
    start_change = 0
    changeList = []

    for row in csv_reader:
    	# Problem 1 
        row_count = start_row_count + 1
        start_row_count = row_count

        # Problem 2
        total = float(start_total) + float(row[1])
        start_total = float(total)

        # Problem 3
        if start_change == 0:
            start_change = float(row[1])
        else:   
            change = float(row[1]) - float(start_change)
            start_change = float(row[1])
            # print(change)
            changeList.append(float(change))

print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total Net Profit/Loss: ${total}")
print(f"Average Change: ${round((sum(changeList)/len(changeList)),2)}")
print(f"Greatest Increase in Profits: (${max(changeList)})")
print(f"Greatest Decrease in Profits: (${min(changeList)})")

with open(output_path, "w") as textfile:
    print("----------------------------", file = textfile)
    print("Financial Analysis", file = textfile)
    print("----------------------------", file = textfile)
    print(f"Total Months: {row_count}", file = textfile)
    print(f"Total Net Profit/Loss: ${total}", file = textfile)
    print(f"Average Change: ${round((sum(changeList)/len(changeList)),2)}", file = textfile)
    print(f"Greatest Increase in Profits: (${max(changeList)})", file = textfile)
    print(f"Greatest Decrease in Profits: (${min(changeList)})", file = textfile)