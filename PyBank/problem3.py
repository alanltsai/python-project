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
    monthList = []
    profitList=[]
    changeList = []

    ###############
    for row in csv_reader:
        if start_change == 0:
            start_change = float(row[1])
            monthList.append(row[0])
            profitList.append(row[1])
            # changeList.append('')
        else:   
            change = float(row[1]) - float(start_change)
            start_change = float(row[1])
            # print(change)
            monthList.append(row[0])
            profitList.append(row[1])
            changeList.append(float(change))

    complete = zip(monthList, profitList, changeList)
    print(complete)
    # print(changeList)
    # print(sum(changeList))
    # print(len(changeList))
    # print(average(changeList))
    print(f"Average Change: {(sum(changeList)/len(changeList))}")
    print(max(changeList))
    print(min(changeList))
    # print(total_change)
    # print(monthList)
    # print(profitList)
