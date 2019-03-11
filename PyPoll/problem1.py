#PyPoll 
import os
import csv

csv_path = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Output","Election_Results.txt")
    
def toPercent(number):
	return round(number * 100,3)

with open(csv_path,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Define Variables
    start_row = 0
    start_khan = 0
    start_correy = 0
    start_li = 0
    start_otooley = 0

    
    for row in csv_reader:
    	# Problem 1
    	row_count = start_row + 1
    	start_row = row_count

    	# Problem 2
    	if row[2] == "Khan":
    		khan_count = int(start_khan) + 1
    		start_khan = khan_count
    	elif row[2] == "Correy":
    		correy_count = int(start_correy) + 1
    		start_correy = correy_count
    	elif row[2] == "Li":
    		li_count = int(start_li) + 1
    		start_li = li_count
    	else:
    		otooley_count = start_otooley + 1
    		start_otooley = otooley_count

    if (khan_count > correy_count) and (khan_count > li_count) and (khan_count > otooley_count):
    	winner = "Khan"
    elif (correy_count > khan_count) and (correy_count > li_count) and (correy_count > otooley_count):
    	winner = "Correy"
    elif (li_count > khan_count) and (li_count > correy_count) and (li_count > otooley_count):
    	winner = "Li"
    elif (otooley_count > khan_count) and (otooley_count > correy_count) and (otooley_count > li_count):
    	winner = "O'Tooley"
    else:
    	winner = "It's a tie between two or more candidates."

    print("----------------------------")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count}")
    print(f"Khan: {toPercent(khan_count/row_count)}% ({khan_count})")
    print(f"Correy: {toPercent(correy_count/row_count)}% ({correy_count})")
    print(f"Li: {toPercent(li_count/row_count)}% ({li_count})")
    print(f"O'Tooley: {toPercent(otooley_count/row_count)}% ({otooley_count})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")
    
    with open(output_path, "w") as textfile:
	    print("----------------------------", file = textfile)
	    print("Election Results", file = textfile)
	    print("----------------------------", file = textfile)
	    print(f"Total Votes: {row_count}", file = textfile)
	    print(f"Khan: {toPercent(khan_count/row_count)}% ({khan_count})", file = textfile)
	    print(f"Correy: {toPercent(correy_count/row_count)}% ({correy_count})", file = textfile)
	    print(f"Li: {toPercent(li_count/row_count)}% ({li_count})", file = textfile)
	    print(f"O'Tooley: {toPercent(otooley_count/row_count)}% ({otooley_count})", file = textfile)
	    print("----------------------------", file = textfile)
	    print(f"Winner: {winner}", file = textfile)
	    print("----------------------------", file = textfile)
