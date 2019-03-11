#PyPoll 
import os
import csv

# Define CSV file path and output file path
csv_path = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Output","Election_Results.txt")

# Define function to convert number to percent    
def toPercent(number):
    return round(number * 100,3)

# Read CSV file
with open(csv_path,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Define Variables
    start_row = 0
    start_khan = 0
    start_correy = 0
    start_li = 0
    start_otooley = 0

    # Loop through each line in CSV file
    for row in csv_reader:
        
        # Add 1 to start_row variable, set start_row as previous count
        row_count = start_row + 1
        start_row = row_count

        # Add 1 to starting counts per person, set starting counts as previous count
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

    # Define winner
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

    # Print statements
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
    
    # Output statements to text file
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
