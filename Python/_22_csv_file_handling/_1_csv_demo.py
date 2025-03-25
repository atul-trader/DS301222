# CSV
# it stands for Comma Seperated Value
# extension .csv
# all the data in this file are seperated by comma

import csv

rows = []
with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_22_csv_file_handling\\test.csv") as file:
    data = csv.reader(file)

    column = next(data) # it will return the row as well as delete the row at the same time
    print("Column : ",column)
    
    for row in data:
        rows.append(row)

    print(rows)

    for i in rows[:2]:
        print(i)

    count = data.line_num
    print("Row count : ",count)

