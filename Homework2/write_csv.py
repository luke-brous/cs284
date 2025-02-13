import csv

# Open csv file and enter write mode
# Automatically closes the csv file 
with open("example.csv", "w") as csvfile:
    # create variable to write in the csv file
    c = csv.writer(csvfile)
    
    # write the column headers as the first line
    c.writerow(['student', 'id'])
    
    # list of lists of data to enter into csvfile
    data = [
            ["John James", 342932],
            ["Donald Donaldson", 309872],
            ["Gerald Geraldi", 203945],
            ["Brock Brocoli", 982315]
    ]

    # iterate through the values in the data list 
    for value in data:
        # write the value to the csv file
        c.writerow(value)


