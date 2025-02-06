import csv

# Open csv file and enter write mode
# Automatically closes the csv file 
with open("presidents.csv", "r", newline='') as csvfile:
    # create variable to write in the csv file
    c = csv.writer(csvfile)
    
    # iterate through the values in the data list 
    for row in c:
        print(row)


