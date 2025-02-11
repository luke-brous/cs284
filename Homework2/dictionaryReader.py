import csv

# Open csv file and enter read mode
# Automatically closes the csv file as well
with open("presidents.csv", "r", newline='') as csvfile:
    # create variable to read the lines in the csv file as a Dicitonary
    c = csv.DictReader(csvfile)
    

    # iterate through the values in the data list 
    for row in c:
        # print the value of the key 
        print(row['President'], ',', row['Party'])


