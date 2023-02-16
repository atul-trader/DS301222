import csv

# # storing data in file using list
# column = ["id","name"]
# rows = [["1","Bharati"],["2","Dhanashri"],["3","Kamleshwar"]]

# with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_22_csv_file_handling\\demo.csv","w") as file:
#     writer = csv.writer(file)
#     writer.writerow(column)
#     writer.writerows(rows)




# storing data in file using dict 
column = ["id","name"]
rows = [{"id":1,"name":"Bharati"},{"id":2,"name":"Raj"}]

with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_22_csv_file_handling\\demo.csv","w") as file:
    writer = csv.DictWriter(file,column)
    writer.writeheader()
    writer.writerows(rows)